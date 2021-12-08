from flask import Blueprint, render_template, request, redirect, \
    url_for, flash, jsonify, make_response, send_from_directory

from . import model
from .utils import projection_to_dict
import datetime, flask_login, os

bp = Blueprint('data', __name__)

#-----------------------------PROFILE IMAGES----------------------------------
@bp.route('/users/src/<img>')
@flask_login.login_required
def get_profile_img(img):
    user = flask_login.current_user
    if img == user.image_path:
        return send_from_directory('src', img)
    else:
        abort(403, "You can not access to the image requested")


#-----------------------------Reservation schedule-----------------------------
@bp.route('/reservation/<int:movie_id>/projections')
def get_projections(movie_id=0):
    print("lol")
    day = int(request.args.get("date"))
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))
    hour = int(request.args.get("hour"))
    min = int(request.args.get("minute"))
    extra_weeks = int(request.args.get("extra_weeks"))
    
    
    # Get the available movie projection for the days of the week
    movie_projections = {i:[] for i in range(7)}

    
    initial_date = datetime.datetime(year, month, day, 8, 59)
    if extra_weeks > 0:
        initial_date = initial_date + datetime.timedelta(weeks=1, 
                                                        days=-initial_date.weekday())
    
    # From the current day of the week to sundays
    for extra_days, i in enumerate(range(initial_date.weekday(), 7)):

        # Lower bound for date
        current_date = initial_date + datetime.timedelta(days=extra_days)

        # Upper bound for date 
        next_date =  current_date + datetime.timedelta(days=1, hours=-8, minutes=-58)

        # Gets all the movie's projections planed for a given day
        # Converts it to a list of dictionaries
        # Stores in the corresponding day in movie_projections
        movie_projections[i] = projection_to_dict(model.Projection.query
                                .filter(model.Projection.movie_id==movie_id)
                                .filter(model.Projection.date > current_date)
                                .filter(model.Projection.date < next_date)
                                .order_by(model.Projection.date)
                                .all())
    print(movie_projections)
    return make_response(jsonify(movie_projections))
