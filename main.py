from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

from . import model

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

<<<<<<< HEAD
@bp.route("/login")
def login():
    return render_template("main/login.html")

=======
@bp.route("/customer")
def user_teemplate():
    user = model.User("lolito", 'lolito@lolito.com', "legoland")
    return render_template("main/user_template.html",user = user)
>>>>>>> e256d5611565f9e6094bfcea39b7c7d73f4fdb28
