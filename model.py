from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    reservations = db.relationship("Reservation", backref="user", lazy=True)
"""
    A user has many reseravtions
	
"""

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    image_path = db.Column(db.String(64), nullable = False)
    trailer_link = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(2000), nullable = True) # instead of synopsis
    duration_hours = db.Column(db.Integer, nullable = False)
    duration_min = db.Column(db.Integer, nullable = False)
    director = db.Column(db.String(64), nullable=False)
    cast = db.Column(db.String(200), nullable = True)
    projections = db.relationship('Projection', backref='movie', lazy = True)
    """
    A movie has many movie projections
    
    """
	


class Screen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seats = db.Column(db.Integer)
    projections = db.relationship('Projection', backref='screen', lazy = True)
    """
    A screen has many movie projections
    
    """

class Projection(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    screen_id = db.Column(db.Integer, db.ForeignKey("screen.id"), nullable = False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), nullable = False)
    date = db.Column(db.DateTime(), nullable=False)
    reservations = db.relationship('Reservation', backref='projection', lazy=True)
    """
    A movie projection has only one movie, one screen, and many reservations
    
    """

class Reservation(db.Model ):
    id = db.Column(db.Integer, primary_key=True)
    projection_id = db.Column(db.Integer, db.ForeignKey("projection.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    """
    A reservation has one user and one mobie projection
    """
