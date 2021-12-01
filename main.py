from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

import datetime

from . import model, db

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    movies = model.Movie.query.all()
    return render_template("main/home.html", movies=movies[:5], all_movies=movies)

#-------------------RESERVATION---------------------------------
@bp.route("/reservation/<int:movie_id>") # Requires the movie id
def reservation(movie_id = 1):
    movie = model.Movie.query.filter_by(id=movie_id).first_or_404()
    return render_template("main/reservation.html", movie=movie)

@bp.route("/reservation/<int:movie_id>", methods=['POST'])
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
        user_id=3,
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

#-----------------------USER--------------------------------------
@bp.route("/user")
def user_template():
    user = model.User.query.filter_by(id=2).first_or_404()

    # If the user is not admin it loads the customer view else the admin view
    if not user.admin:

        # Reservations
        reservations_before = (model.Reservation.query
            .filter_by(user_id=user.id)
            .filter(model.Reservation.date < datetime.datetime.now())
            .order_by(model.Reservation.date)
            .all()
        )

        reservations_after = (model.Reservation.query
            .filter_by(user_id=user.id)
            .filter(model.Reservation.date >= datetime.datetime.now())
            .order_by(model.Reservation.date)
            .all()
        )
        return render_template("main/user_template.html",
            user=user,
            reservations_after=reservations_after,
            reservations_before=reservations_before)
    else:
        movies = model.Movie.query.all()
        screens = model.Screen.query.all()
        return render_template("main/admin_template.html",
            movies=movies,
            screens=screens,
            user=user)

@bp.route("/user", methods=["POST"])
def post_user():
    # Logic of web site review and movie projection creation
    
    user = model.User.query.filter_by(id=1).first()
    if not user.admin:
        pass #reviews
    else:
        movie_id = int(request.form.get("movie"))
        screen_id = int(request.form.get("screen"))
        date_ = request.form.get("date")+" " + request.form.get("time")
        date = datetime.datetime.strptime(date_, '%Y-%m-%d %H:%M')

    return redirect(url_for("main.user_template"))

#----------------------LOGIN--------------------------------------
@bp.route("/login")
def login():
    return render_template("main/login.html")

#-----------------------SIGNUP--------------------------------------
@bp.route("/register")
def register():
    return render_template("main/register.html")