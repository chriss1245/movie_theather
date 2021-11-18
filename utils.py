import datetime
def date_to_dict(date: datetime.datetime) -> dict:
    date_dict = {
        'hour': date.hour,
        'minute': date.minute,
        'day': date.day,
        'month': date.month,
        'year': date.year,
        'weekday': date.weekday() #datetime.weekday() returns mon = 0.. sun = 6
    }
    return date_dict

def projection_to_dict(movie_projection) -> dict:
    """
    """
    projection_dict = {
        "id":movie_projection.id,
        "screen": movie_projection.screen_id,
        "duration": movie_projection.movie.duration_hours,
        "duration_min": movie_projection.movie.duration_min,
        "hour": movie_projection.date.hour,
        "minute": movie_projection.date.minute,
        "day": movie_projection.date.weekday(),
        }

    return projection_dict