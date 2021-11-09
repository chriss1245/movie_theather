from flask import Blueprint, render_template, request, redirect, \
    url_for, flash, jsonify, make_response

bp = Blueprint('data', __name__)

#-----------------------------Reservation schedule-----------------------------
@bp.route('/data/reservation')
def data_reservation():
    
    return make_response(jsonify([{"message":'lol'}, {"message":'lel'}]))