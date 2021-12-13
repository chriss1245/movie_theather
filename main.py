from flask import Blueprint, render_template, request, url_for, \
    redirect, abort, flash
from . import model, db, bcrypt, analytics, csrf
import flask_login, datetime, imghdr, os
from .utils import cancellation_emails, reservation_email
from werkzeug.utils import secure_filename, send_from_directory
bp = Blueprint("main", __name__)

#-----------------------------HOME-------------------------------------------------
@bp.route("/")
def home():
    movies = model.Movie.query.order_by(model.Movie.rating.desc()).limit(5).all() # Gets the 5 best rated movies
    movies.append(movies[0]) # Needed for the slider animation 
    all_movies = model.Movie.query.order_by(model.Movie.id.desc()).all() # All movies by newest
    return render_template("main/home.html", movies=movies, all_movies=all_movies)

#-----------------------------SEARCH----------------------------------------------
@bp.route("/search")
def search():
    order_criteria = request.args.get("sort_by")
    str = request.args.get("search_text")
    all_movies = []
    # Makes a query depending on the search criteria
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
@csrf.exempt # avoids flask seasurf protection
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
    reservation_email(reservation)
    return redirect(url_for('main.user_template'))

#----------------------PROJECTION------------------------------
@bp.route("/projection/<int:projection_id>")
@flask_login.login_required
def projection(projection_id=1):
    user = flask_login.current_user
    if user.admin:
        projection = model.Projection.query.filter_by(id=projection_id).first_or_404()

        free_seats = projection.screen.seats
        reserved_seats = 0
        for reservation in projection.reservations:
            free_seats -= reservation.seats
            reserved_seats += reservation.seats
        
        img = analytics.seats_available({'Projection: ' + str(projection.id): (free_seats, reserved_seats)})
        return render_template("main/projection.html", projection=projection, user=user,  analytics_plot=img.decode('utf-8'))
    abort(403, "You do not have the correct permissions")

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

        reservations_before = [] # Seen
        reservations_after = [] # To See
        for reservation in reservations:
            if reservation.projection.date <= datetime.datetime.now():
                reservations_before.append(reservation)
            else:
                reservations_after.append(reservation)
        return render_template("main/user_template.html",
            user=user,
            reservations_after=reservations_after,
            reservations_before=reservations_before)

    # If user is admin
    # Get the movies, the sceens, the reviews, and analytics plots
    movies = model.Movie.query.order_by(model.Movie.rating).all()
    screens = model.Screen.query.all()
    reviews = model.Review.query.all()
    web_analitics_plot = analytics.web_analytics(reviews)  
    movie_analytics_plot = analytics.movie_analytics({movie.name: movie.rating for movie in movies})

    # Programmed projecitons
    projections = (model.Projection.query
        .filter(model.Projection.date > datetime.datetime.now())
        .all())
    
    data = {}
    for projection in projections:
        free_seats = projection.screen.seats
        reserved_seats = 0
        for reservation in projection.reservations:
            free_seats -= reservation.seats
            reserved_seats += reservation.seats
            data[str(projection.movie.name) + ", room " + str(projection.screen.id) +", " + str(projection.date)[:-9]] = (free_seats, reserved_seats)
    print(data)
    img = analytics.seats_available(data, figsize=(6,int(len(data)*0.9)))
    
    return render_template("main/admin_template.html",
        movies=movies,
        screens=screens,
        user=user,
        analytics_plot=web_analitics_plot.decode('utf-8'),
        analytics_movie=movie_analytics_plot.decode('utf-8'),
        projections_plot=img.decode('utf-8'),
        projections=projections)

@bp.route("/user", methods=["POST"])
@flask_login.login_required
def post_user():
    # Logic of web site review and movie projection creation
    user = flask_login.current_user
    form_type = request.form.get("type")

    # Both users can upload a profile picture
    if form_type == "upload_picture":
        file = request.files['img']
        if imghdr.what(file): #Checks the image is recognized
            path = secure_filename(file.filename) # filters weird paths
            if user.image_path: # if there is another image, remove it
                try:
                    os.remove(os.path.join('src', user.image_path))
                except:
                    pass
            user.image_path = path
            db.session.commit()
            path = os.path.join('src', path)
            file.save(path)

        else:
            abort(403, "Forbidden file")
    
    # Normal users can not add movie projections
    if not user.admin: 
        if form_type == "feedback":
            # Reviews
            text = request.form.get("feedback")
            new_review = model.Review(text=text)
            db.session.add(new_review)
            db.session.commit()
        elif form_type == "cancel":
            # Cancelations of reservations
            reservation_id = int(request.form.get("reservation_id"))
            reservation = model.Reservation.query.filter_by(id=reservation_id).first_or_404()
            cancellation_emails([reservation])
            reservation = model.Reservation.query.filter_by(id=reservation_id).delete()
            db.session.commit()

    # Admin can not cancel reservations or give feedback     
    else:
        if form_type == "new_projection":
            movie_id = int(request.form.get("movie"))
            screen_id = int(request.form.get("screen"))
            date_ = request.form.get("date")+" " + request.form.get("time")
            date = datetime.datetime.strptime(date_, '%Y-%m-%d %H:%M')

            # Get projections on screen 2 hours and 30 minutes after or before 
            existent_projection = (model.Projection.query
                .filter_by(screen_id=screen_id)
                .filter(model.Projection.date >= date - datetime.timedelta(hours=-2, minutes=-30))
                .filter(model.Projection.date <= date + datetime.timedelta(hours=-2, minutes=-30))
                .first()
            )
            if existent_projection:
                abort(403, "Screen is already used by other movie projection")

            # Create projection
            projection = model.Projection(screen_id=screen_id, movie_id=movie_id, date=date)
            db.session.add(projection)
            db.session.commit()
        elif form_type == "cancel":
            projection_id = int(request.form.get("projection_id"))
            projection = model.Projection.query.filter_by(id=projection_id).first_or_404()
            cancellation_emails(projection.reservations)
            model.Projection.query.filter_by(id=projection_id).delete()
            db.session.commit()

    return redirect(url_for("main.user_template"))
