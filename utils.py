import datetime

def projection_to_dict(movie_projections) -> dict:
    """
    """
    projections = []

    for movie_projection in movie_projections:
        projections.append({
            "id":movie_projection.id,
            "screen": movie_projection.screen_id,
            "duration": movie_projection.movie.duration_hours,
            "duration_min":movie_projection.movie.duration_min,
            "hour": movie_projection.date.hour,
            "min": movie_projection.date.minute,
            "day": movie_projection.date.day,
            "month": movie_projection.date.strftime('%B'),
            "year":movie_projection.date.year
            })
    
    #{hour:11, min:3, duration:2, duration_min:23, title:"joker", id:1, day:23, month:"October", year:2021}

    return projections 