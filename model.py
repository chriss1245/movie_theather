class Movie():
    def __init__(self, id, name, image_path, duration=0, director= "", cast="", description = " ", trailer_link = '0'):
        self.id = id
        self.name = name
        self.image_path = image_path
        self.duration = duration
        self.director= director
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
    def __init__(self, name, email,password="" ,location):
        self.name = name
        self.email = email
        self.password = password
        self.location = location
