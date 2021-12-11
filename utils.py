import datetime
from flask_mail import Message
from __init__ import mail

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

def reservation_email(reservation):
    movie_name = reservation.projection.movie.name
    movie_date = reservation.projection.date


def cancellation_emails(reservations):
    movie_name = reservations[0].projection.movie.name
    movie_projection_date = reservations[0].projection.date
    subject = "Cancelled Projection on " + movie_projection_date
    recipients = [(reservation.user.email, reservation.user.name, reservation.seats) for reservation in reservations]
    for email, name, seats in recipients:
        msg_body = "Hello "+ name + "\nSadly a projection in which you had made a reservation has been cancelled.\nDetails are:\n\t movie name: " + movie_name + "\n\tMovie_date: " + movie_projection_date + "\n\tSeats: " + seats
        message = Message( recipients=[email], body=msg_body, subject=subject)
        mail.send(message)

