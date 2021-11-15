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
<<<<<<< HEAD

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
=======
>>>>>>> e256d5611565f9e6094bfcea39b7c7d73f4fdb28

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
