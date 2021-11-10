class Movie():
    def __init__(self, id, name, image_path, description = " ", trailer_link = '0'):
        self.id = id
        self.name = name
        self.image_path = image_path
        self.description = description
        self.trailer_link = trailer_link
class Screen():
    def __init__(self, id):
        self.id = id

class MoviePorjection():
    def  __init__(self, id, screen_id, movie_id, date):
        self.id = id
        self.screen_id = screen_id
        self.movie_id = movie_id
        self.date = date