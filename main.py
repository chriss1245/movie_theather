from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

import datetime

from . import model, db

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    movies = model.Movie.query.all()
    return render_template("main/home.html", movies=movies[:5], all_movies=movies)

@bp.route("/reservation/<int:movie_id>") # Requires the movie id
def reservation(movie_id = 1):
    movie = model.Movie.query.filter_by(id=movie_id).first_or_404()
    return render_template("main/reservation.html", movie=movie)

@bp.route("/reservation/<int:movie_id>", methods=['POST'])
def post_reservation(movie_id= 0):

    # Get the projection
    projection_id = int(request.form.get("movie_projection_id"))
    projection = model.Projection.query.filter_by(id=projection_id).first_or_404()
    
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
        user_id=1,
        seats=seats,
        date=datetime.datetime.now()
    )
    db.session.add(reservation)
    db.session.commit()
    return redirect(url_for('main.user_template'))

@bp.route("/movie/<int:movie_id>") # will take the movie id
def movie(movie_id=1):
    movie = model.Movie.query.filter_by(id=movie_id).first_or_404()
    return render_template("main/movie.html", movie=movie)

@bp.route("/login")
def login():
    return render_template("main/login.html")

@bp.route("/customer")
def user_template():
    return render_template("main/user_template.html",user = None, movies_after = [], movies_before = [])


@bp.route("/register")
def register():
    return render_template("main/register.html")
