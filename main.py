from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    movies = [ model.Movie(i, name, 'img/'+str(i)+'.jpg') for i, name, in zip(range(1,12), ['Black panter', 'After', 'Star Wars ', 'Justice league', 'Jaws', 'Joker', 'It', 'Titanic', 'Harry Potter', "Avatar", "Butterfly Effect"])]
    return render_template("main/home.html", movies=movies[5:], all_movies=movies)