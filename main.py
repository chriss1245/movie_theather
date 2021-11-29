from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    movies = model.Movie.query.all()
    return render_template("main/home.html", movies=movies[:5], all_movies=movies)

@bp.route("/reservation/<int:movie_id>") # Requires the movie id
def reservation(movie_id = 1):
    movie = model.Movie(1, "Harry potter and the Chamber of Secrets", 'img/1.jpg')
    return render_template("main/reservation.html", movie=movie)

@bp.route("/reservation/<int:movie_id>", methods=['POST'])
def post_reservation(movie_id= 0):
    projection_id = request.form.get("movie_projection_id")
    return redirect(url_for('main.home'))

@bp.route("/movie/<int:movie_id>") # will take the movie id
def movie(movie_id=1):

    return render_template("main/movie.html")

@bp.route("/login")
def login():
    return render_template("main/login.html")

@bp.route("/customer")
def user_template():
    return render_template("main/user_template.html",user = None, movies_after = [], movies_before = [])


@bp.route("/register")
def register():
    return render_template("main/register.html")
