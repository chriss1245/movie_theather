from flask import Blueprint, render_template, request, url_for, \
    redirect, abort

from . import model

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    movies = [ model.Movie(i, name, 'img/'+str(i)+'.jpg') for i, name, in zip(range(1,6), ['Black panter', 'After', 'Star Wars ', 'Justice league', 'It'])]
    return render_template("main/home.html", movies=movies)