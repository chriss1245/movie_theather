from flask import Blueprint, render_template, request, url_for, \
    redirect, abort, make_response

from flask_wtf import CSRFProtect
from flask_talisman import Talisman
from . import model


bp = Blueprint("main", __name__)

# directive for cross site request forgery
csrf = CSRFProtect(bp)

# content secure policy directives
csp = {
    'default-src': '\'self\'',
}

#disables access to geolocation interface
feature_policy = {
    'geolocation': '\'none\''
}

permissions_policy = {
    'microphone':'()'
}

talisman = Talisman(bp, content_security_policy = csp, feature_policy = feature_policy, permission_policy = permissions_policy)

@bp.route("/")
def home():
    movies = [ model.Movie(i, name, 'img/'+str(i)+'.jpg') for i, name, in zip(range(1,12), ['Black panther', 'After', 'Star Wars ', 'Justice league', 'Jaws', 'Joker', 'It', 'Titanic', 'Harry Potter', "Avatar", "Butterfly Effect"])]
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
    movie = model.Movie(1, "Harry potter and the Chamber of Secrets", 'img/9.jpg',2, 30, "director", "cast", "description", 'https://www.youtube.com/embed/jBltxS8HfQ4')
    return render_template("main/movie.html", movie=movie)

@bp.route("/login")
def login():
    return render_template("main/login.html")

# we only want to add files (profile picture) in the user_template
@bp.route("/customer")
@talisman(
    content_security_policy = {
        'default-src': '\'self\'',
        'img-src': '*',
        'script-src': '\'self\''
    },
    feature_policy = feature_policy
)
def user_template():
    user = model.User("lolito", 'lolito@lolito.com', "legoland")
    return render_template("main/user_template.html",user = user, movies_after = [], movies_before = [])


@bp.route("/register")
def register():
    return render_template("main/register.html")

