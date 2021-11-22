import datetime

def projection_to_dict(movie_projection, screen, movie) -> dict:
    """
    """
    projection_dict = {
        "id":movie_projection.id,
        "screen": movie_projection.screen_id,
        "duration": movie.duration_hours,
        "duration_min":movie.duration_min,
        "hour": movie_projection.date.hour,
        "min": movie_projection.date.minute,
        "day": movie_projection.date.day,
        "month": movie_projection.date.strftime('%B'),
        "year":movie_projection.date.year
        }
    
    #{hour:11, min:3, duration:2, duration_min:23, title:"joker", id:1, day:23, month:"October", year:2021}

    return projection_dict  