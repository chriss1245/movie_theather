class Movie():
    def __init__(self, id, name, image_path, duration, director, cast, description = " ", trailer_link = '0'):
        self.id = id
        self.name = name
        self.image_path = image_path
        self.duration = duration
        self.director
        self.cast = cast
        self.description = description
        self.trailer_link = trailer_link
class Screen():
    def __init__(self, id):
        self.id = id

class MovieProjection():
    def  __init__(self, id, screen_id, movie_id, date):
        self.id = id
        self.screen_id = screen_id
        self.movie_id = movie_id
        self.date = date

class User():
    def __init__(self, name, email, location):
        self.name = name
        self.email = email
        self.location = location


	movie=Movie(db.Model).name
	screen=Screen(db.Model).name
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
	projection=Projection(db.Model).movie
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
