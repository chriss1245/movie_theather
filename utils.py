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
    subject = "Reservation processed correctly"
    msg_body = "Hello " + reservation.user.name + "\nYour reservation on " + " was processed correctly" + "\nDetails" + "\n\tMovie name: " + movie_name + "\n\tMovie date: " + movie_date
    message = Message(recipients=[reservation.user.email], body=msg_body, subject=subject)
    mail.send(message)

def cancellation_emails(reservations):
    # receives a list of reservation objects
    movie_name = reservations[0].projection.movie.name
    movie_projection_date = reservations[0].projection.date
    info = [(reservation.user.email, reservation.user.name, reservation.seats, reservation.date) for reservation in reservations]
    for email, name, seats, date in info:
        subject = "Reservation made in " + date + "has been cancelled"
        msg_body = "Hello "+ name + "\nSadly a projection in which you had made a reservation has been cancelled.\nDetails\n\tMovie name: " + movie_name + "\n\tMovie date: " + movie_projection_date + "\n\tSeats: " + seats
        message = Message( recipients=[email], body=msg_body, subject=subject)
        mail.send(message)

