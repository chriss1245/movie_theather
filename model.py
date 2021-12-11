import datetime


class Movie():
    def __init__(self, id, name, image_path, duration_hours=1, duration_min = 45, director= "", cast="", description = " ", trailer_link = '0'):
        self.id = id
        self.name = name
        self.image_path = image_path
        self.duration_hours = duration_hours
        self.duration_min = duration_min
        self.director= director
        self.cast = cast
        self.description = description
        self.trailer_link = trailer_link

class Screen():
    def __init__(self, id):
        self.id = id

class MovieProjection():
    def  __init__(self, id, screen_id, movie_id, movie, screen):
        self.id = id
        self.screen_id = screen_id
        self.movie_id = movie_id
        self.date = datetime.datetime.now()
        self.movie = movie
        self.screen = screen

class User():
    def __init__(self, name, email,password="" ,location="", isAdmin=False):
        self.name = name
        self.email = email
        self.password = password
        self.location = location
        self.is_admin = isAdmin



class Review():
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.date = datetime.datetime.now()

class Reservation():
    def __init__(self, user, projection):
        self.projection = projection
        self.seats = 5
        self.user = user
        self.projection = projection
        self.date = datetime.datetime.now()