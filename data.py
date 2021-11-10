from flask import Blueprint, render_template, request, redirect, \
    url_for, flash, jsonify, make_response

from .model import MoviePorjection, Movie, Screen
from .utils import date_to_dict
import datetime

bp = Blueprint('data', __name__)

#-----------------------------Reservation schedule-----------------------------
@bp.route('/data/reservation')
def data_reservation():
    date = datetime.datetime(2019, 4, 18, 14, 0) # year, month, day, hour, min
    date2 = datetime.datetime(2021, 11, 9, 13, 29)
    movie = Movie(1, "Joker", "img/1.jpg")
    screens = [Screen(1), Screen(12)]
    dates = [date, date2]
    mp1 = MoviePorjection(1, 1, 1, date)
    mp1 = MoviePorjection(1, 1, 1, date2)

    movie_projections  = [{'screen':1, 'date':date_to_dict(date)},
    {'screen':2, 'date':date_to_dict(date2)}] #ignored movie, since it is already gotten from movie view
    return make_response(jsonify(movie_projections))

