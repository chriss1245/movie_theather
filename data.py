from flask import Blueprint, render_template, request, redirect, \
    url_for, flash, jsonify, make_response

from . import model
from .utils import projection_to_dict
import datetime
from calendar import monthrange

bp = Blueprint('data', __name__)

#-----------------------------Reservation schedule-----------------------------
@bp.route('/reservation/<int:movie_id>/projections')
def get_projections(movie_id=0):
    day = int(request.args.get("date"))
    month = int(request.args.get("month"))
    year = int(request.args.get("year"))
    hour = int(request.args.get("hour"))
    min = int(request.args.get("minute"))
    
    
    # Get the available movie projection for the days of the week
    movie_projections = {i:[] for i in range(7)}
    days_in_month = monthrange(year, month)[-1]
    
    for extra_days, i in enumerate(range(datetime.datetime(year, month, day).weekday(), 7)):
        
        # Gives a valid date
        if day + extra_days > days_in_month:
            day_ = ((day + extra_days) % (days_in_month + 1)) + 1

            if month + 1 > 12:
                year_ = year + 1
                month_ = 1
            else:
                month_ = month + 1
        else:
            month_ = month
            day_ = day + extra_days
            year_ = year

        current_date = datetime.datetime(year_, month_, day_, hour, min)
        """Check the filter by"""
        next_date =  current_date + datetime.timedelta(days=1)
        
        movie_projections[i] = projection_to_dict(model.Projection.query
                                .filter(movie_id==movie_id)
                                .filter(model.Projection.date >= current_date)
                                .filter(model.Projection.date <= next_date)
                                .order_by(model.Projection.date)
                                .all())
    
    print(movie_projections)    
    return make_response(jsonify(movie_projections))
