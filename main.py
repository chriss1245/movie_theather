from flask import Blueprint, render_template, request, url_for, \
    redirect, abort, flash

import flask_login
import datetime
from werkzeug.utils import secure_filename, send_from_directory

import matplotlib.pyplot as plt

from . import model, db, bcrypt, analytics


bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    flask_login.login_user(model.User.query.filter_by(id=3).first())
    movies = model.Movie.query.order_by(model.Movie.rating.desc()).limit(5).all()
    movies.append(movies[0])
    all_movies = model.Movie.query.order_by(model.Movie.id.desc()).all()
    return render_template("main/home.html", movies=movies, all_movies=all_movies)

@bp.route("/search")
def search():
    order_criteria = request.args.get("sort_by")
    str = request.args.get("search_text")
    all_movies = [] 
    if order_criteria ==  "newest":
        all_movies = (model.Movie.query
            .filter(model.Movie.name.startswith(str))
            .order_by(model.Movie.id.desc())
            .all())
    elif order_criteria == "oldest":
        all_movies = (model.Movie.query
            .filter(model.Movie.name.startswith(str))
            .order_by(model.Movie.id.desc())
            .all())
    elif order_criteria == "shortest":
        all_movies = (model.Movie.query
            .filter(model.Movie.name.startswith(str))
            .order_by(model.Movie.duration_hours, model.Movie.duration_min)
            .all())
    elif order_criteria == "longest":
        all_movies = (model.Movie.query
            .filter(model.Movie.name.startswith(str))
            .order_by(model.Movie.duration_hours.desc(), model.Movie.duration_min.desc())
            .all())
    return render_template("main/search.html", all_movies=all_movies)

#-------------------RESERVATION---------------------------------
@bp.route("/reservation/<int:movie_id>") # Requires the movie id
@flask_login.login_required
def reservation(movie_id = 1):
    movie = model.Movie.query.filter_by(id=movie_id).first_or_404()
    return render_template("main/reservation.html", movie=movie)

@bp.route("/reservation/<int:movie_id>", methods=['POST'])
@flask_login.login_required
def post_reservation(movie_id= 0):
    # Get the projection
    projection_id = int(request.form.get("movie_projection_id"))
    projection = (model.Projection.query
        .filter_by(id=projection_id)
        .filter(model.Projection.date >= datetime.datetime.now())
        .first())
    if not projection:
        abort(403, "Movie projection not available, try another")
    
    # Get the remaining seats in the movie projection
    remaining_seats = projection.screen.seats
    for reservation in projection.reservations:
        remaining_seats -= reservation.seats
    
    # Check whether are enough seats before of doing a reservation
    seats = int(request.form.get("number_seats"))
    if remaining_seats < seats:
        abort(403, f"There are not enough seats, try another projection (only: {remaining_seats} seats available)")
    
    # Proceed with the reservation
    reservation = model.Reservation(
        projection_id=projection.id,
        user_id=flask_login.current_user.id,
        seats=seats,
        date=datetime.datetime.now()
    )
    db.session.add(reservation)
    db.session.commit()
    return redirect(url_for('main.user_template'))

#-----------------------MOVIE----------------------------------
@bp.route("/movie/<int:movie_id>") # will take the movie id
def movie(movie_id=1):
    movie = model.Movie.query.filter_by(id=movie_id).first_or_404()
    return render_template("main/movie.html", movie=movie)

# Updates the rating of the movie
@bp.route("/movie/<int:movie_id>", methods=["POST"])
def post_movie(movie_id):

    # PROTECTION AGAINST INVALID RATINGS
    new_rating = int(request.form.get("rank"))
    if new_rating < 0 or new_rating > 5:
        abort(403, "Not a valid rating")

    movie = model.Movie.query.filter_by(id=movie_id).first_or_404()

    # Update the mean of the ratings
    movie.rating = (movie.rating * movie.ratings + new_rating ) / (movie.ratings + 1)
    print(movie.rating)
    # Update the number of ratings
    movie.ratings += 1
    db.session.commit()
    
    return redirect(url_for("main.movie", movie_id=movie_id))

#-----------------------USER--------------------------------------
@bp.route("/user")
@flask_login.login_required
def user_template():
    user = flask_login.current_user

    # If the user is not admin it loads the customer view else the admin view
    if not user.admin:

        # Reservations
        reservations = (model.Reservation.query
            .filter_by(user_id=user.id)
            .order_by(model.Reservation.date)
            .all()
        )

        reservations_before = []
        reservations_after = []
        for reservation in reservations:
            if reservation.projection.date <= datetime.datetime.now():
                reservations_before.append(reservation)
            else:
                reservations_after.append(reservation)

        return render_template("main/user_template.html",
            user=user,
            reservations_after=reservations_after,
            reservations_before=reservations_before)
    
    movies = model.Movie.query.all()
    screens = model.Screen.query.all()
    reviews = model.Review.query.all()
    web_analitics_plot = analytics.web_analytics(reviews)  
    return render_template("main/admin_template.html",
        movies=movies,
        screens=screens,
        user=user, analytics_plot=web_analitics_plot.decode('utf-8'))

@bp.route("/user", methods=["POST"])
@flask_login.login_required
def post_user():
    # Logic of web site review and movie projection creation
    user = flask_login.current_user
    form_type = request.form.get("type")
    if not user.admin:
        if form_type == "feedback":
            # Handling reviews
            text = request.form.get("feedback")
            new_review = model.Review(text=text)
            db.session.add(new_review)
            db.session.commit()
        elif form_type == "upload_picture":
            img = secure_filename(request.form.get("img"))
            send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
            print(type(img))
            
        elif form_type == "cancel":
            reservation_id = int(request.form.get("reservation_id"))
            reservation = model.Reservation.query.filter_by(id=reservation_id).delete()
                 
    else:
        if type == "new_projection":
            movie_id = int(request.form.get("movie"))
            screen_id = int(request.form.get("screen"))
            date_ = request.form.get("date")+" " + request.form.get("time")
            date = datetime.datetime.strptime(date_, '%Y-%m-%d %H:%M')

            existent_projection = (model.Projection.query
                .filter_by(screen_id=screen_id)
                .filter(model.Projection.date >= date - datetime.timedelta(hours=-2, minutes=-30))
                .filter(model.Projection.date <= date + datetime.timedelta(hours=-2, minutes=-30))
                .first()
            )
            if existent_projection:
                abort(403, "Screen is already used by other movie projection")

            projection = model.Projection(screen_id=screen_id, movie_id=movie_id, date=date)
            db.session.add(projection)
            db.session.commit()
        elif type == "upload_picture":
            pass
    return redirect(url_for("main.user_template"))

#----------------------LOGIN--------------------------------------
@bp.route("/login")
def login():
    return render_template("main/login.html")

@bp.route("/login", methods=["POST"])
def post_login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = model.User.query.filter_by(email=email).first()

    """
    if user and bcrypt.check_password_hash(user.password, password):
        flask_login.login_user(user)
        return redirect(url_for('main.index'))
    else:
        flash('Wrong email or password. Try again')"""
    flask_login.login_user(user)
    return redirect(url_for('main.user_template'))

#-----------------------SIGNUP--------------------------------------
@bp.route("/register")
def register():
    return render_template("main/register.html")

@bp.route("/register", methods=["POST"])
def post_register():
    email = request.form.get('email')
    username = request.form.get('name')
    password = request.form.get('password')
    
    # Equal passwor/singup/singupds
    if  password != request.form.get('password_repeat'):
        flash("Passwords differ")
        return redirect(url_for("main.register"))
    
    # Check if the email is already at the database
    user = model.User.query.filter_by(email = email).first()
    if user:
        flash('User already exists') 
        return redirect(url_for("main.register"))

    #password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    password_hash=password
    new_user = model.User(email=email, name=username, password = password_hash, admin=False)

    db.session.add(new_user)
    db.session.commit()
    flask_login.login_user(new_user)
    return redirect(url_for('main.user_template'))

#-------------------------LOGOUT---------------------------------------
@bp.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('main.home'))