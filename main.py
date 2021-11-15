from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

from .model import Movie, MoviePorjection, Screen

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    movies = [ model.Movie(i, name, 'img/'+str(i)+'.jpg') for i, name, in zip(range(1,12), ['Black panther', 'After', 'Star Wars ', 'Justice league', 'Jaws', 'Joker', 'It', 'Titanic', 'Harry Potter', "Avatar", "Butterfly Effect"])]
    return render_template("main/home.html", movies=movies[5:], all_movies=movies)

@bp.route("/reservation") # Requires the movie id
def reservation(movie_id = 1):
    return render_template("main/reservation.html")

@bp.route("/movie") # will take the movie id
def movie(movie_id = 1):
    return render_template("main/movie.html")

@bp.route("/login")
def login():
    return render_template("main/login.html")

