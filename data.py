from flask import Blueprint, render_template, request, redirect, \
    url_for, flash, jsonify, make_response

from .model import Projection, Movie, Screen
from .utils import projection_to_dict
import datetime

bp = Blueprint('data', __name__)

#-----------------------------Reservation schedule-----------------------------
@bp.route('/reservation/<int:movie_id>/projections')
def get_projections(movie_id=0):
    day = int(request.args.get("date"))
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))
    hour = int(request.args.get("hour"))
    min = int(request.args.get("minute"))

    initial_date = datetime.datetime(year, month, day, hour, min)
    print(initial_date)
    date = datetime.datetime(2019, 4, 18, 14, 0) # year, month, day, hour, min
    date2 = datetime.datetime(2019, 4, 18, 16, 29)
    date3 = datetime.datetime(2019, 4, 20, 16, 29)
    movie = Movie(1, "Joker", "img/1.jpg")
    screens = [Screen(1), Screen(12)]
    dates = [date, date2, date3]
    mp1 = MovieProjection(1, 1, 1, date)
    mp2 = MovieProjection(1, 1, 1, date2)
    movie_projections = {0:[projection_to_dict(mp1, screens[0], movie), projection_to_dict(mp2, screens[1], movie)],
                        1:[],
                        2: [projection_to_dict(mp1, screens[0], movie), projection_to_dict(mp2, screens[1], movie)],
                        3:[], 4:[], 5:[], 6:[]
                        }
    
    return make_response(jsonify(movie_projections))
