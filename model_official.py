from . import db

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	image_path = db.Column(db.String(64), )
	synopsyis = db.Column(db.String(2000), nullable = False)
	duration_hours = db.Column(db.Integer, nullable = False)
	duration_min = db.Column(db.Integer, nullable = False)
	director = db.Column(db.String(64), nullable=False)
	main_cast = db.Column(db.String(200))
	

	"""
        self.id = id
        self.name = name
        self.image_path = image_path
		self.trailer_path=trailer_path
		self.sypnosis=sypsnosis
		self.duration=duration
		self.director=director
		self.main_cast=main_cast
	"""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Screen(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	seats = db.Column(db.Integer)
	"""
	def __init__(self, name, seats):
		self.name = name
		self.seats = seats
	"""

class Projection(db.Model):

    movie = db.Column(db.String(64), db.ForeignKey('movie.name'), nullable=False)
    screen=db.Column(db.String(64), db.ForeignKey('movie.name'), nullable=False) # Screen(db.Model).name
	
    day=db.Column(db.Integer, primary_key=True)
    hour=db.Column(db.Integer, primary_key=True)
    minute=db.Column(db.Integer, primary_key=True)



    """
    def __init__(self, movie, screen, day, time):
		self.movie=movie
		self.screen=screen
		self.day=day
		self.time=time
	"""

class Reservation(db.Model ):

	user=User(db.Model).email
	movie_projection_id = db.Column(db.Integer, foreign)
	no_seats=db.Column(db.Integer, primary_key=True)
	day_res=db.Column(db.Integer, primary_key=True)
	hour_res=db.Column(db.Integer, primary_key=True)
	minute_res=db.Column(db.Integer, primary_key=True)
	"""
	def __init__(self, user, projection, no_seats, day_res, time_res):
		self.user=user
		self.projection=projection
		self.no_seats=no_seats
		self.day_res=day_res
		self.time_res=time_res

	"""
