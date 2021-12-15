import datetime
from flask_mail import Message
# from . import mail


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




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

def reservation_email(reservation):
    # receives object of type reservation
    movie_name = reservation.projection.movie.name
    movie_date = reservation.projection.date
    subject = "Reservation processed correctly"
    footer = "Thank you for performing a reservation with us.\nKindly\nCinema Carlos III"
    msg_body = "Hello " + reservation.user.name + "\nYour reservation on " + " was processed correctly" + "\nDetails" + "\n\tMovie name: " + movie_name + "\n\tMovie date: " + str(movie_date)
    msg_body += footer
    sender_address = 'CinemaCarlosiii@gmail.com'
    sender_pass = "ProyectoWebApps"
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = reservation.user.email
    message['Subject'] = subject  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(msg_body, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, reservation.user.email, text)
    session.quit()



# this function allows and body
def individual_cancellation(reservation, msg_body):
    subject = "Your reservation has been cancelled"
    # receives object of type reservation
    movie_name = reservation.projection.movie.name
    movie_date = reservation.projection.date
    details = "\nDetails" + "\n\tMovie name: " + movie_name + "\n\tMovie date: " + str(
        movie_date)
    footer = "Thank you for performing a reservation with us.\nKindly\nCinema Carlos III"
    sender_address = 'CinemaCarlosiii@gmail.com'
    sender_pass = "ProyectoWebApps"
    # Setup the MIME
    msg_body = "Hello\n" + msg_body
    msg_body += (details + footer)
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = reservation.user.email
    message['Subject'] = subject  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(msg_body, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, reservation.user.email, text)
    session.quit()

def non_zero(func):
    def wrapper(*args, **kwargs):
        if len(args[0]) == 0:
            return
        else:
            res = func(*args, **kwargs)
        return res
    return wrapper


def cancellation_emails(reservations):
    if len(reservations) == 0:
        return
    movie_name = reservations[0].projection.movie.name
    movie_projection_date = str(reservations[0].projection.date)
    info = [(reservation.user.email, reservation.user.name, str(reservation.seats), str(reservation.date)) for reservation in reservations]
    sender_address = 'CinemaCarlosiii@gmail.com'
    sender_pass = "ProyectoWebApps"
    footer = "Thank you for performing a reservation with us.\nKindly\nCinema Carlos III"
    # Setup the MIME
    message = MIMEMultipart()
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    
    for email, name, seats, date in info:
        try:
            subject = "Reservation made in " + str(date) + "has been cancelled"
            msg_body = "Hello " + name + "\nSadly a projection in which you had made a reservation has been cancelled.\nDetails\n\tMovie name: " + movie_name + "\n\tMovie date: " + movie_projection_date + "\n\tSeats: " + str(seats)
            msg_body += footer
            message['From'] = sender_address
            message['To'] = email
            message['Subject'] = subject  # The subject line
            # The body and the attachments for the mail
            message.attach(MIMEText(msg_body, 'plain'))
            text = message.as_string()
            session.sendmail(sender_address, email, text)
        except:
            ...

    session.quit()

"""

def reservation_email(reservation):
    movie_name = reservation.projection.movie.name
    movie_date = reservation.projection.date
    subject = "Reservation processed correctly"
    msg_body = "Hello " + reservation.user.name + "\nYour reservation on " + " was processed correctly" + "\nDetails" + "\n\tMovie name: " + movie_name + "\n\tMovie date: " + str(movie_date)
    message = Message(recipients=[reservation.user.email], body=msg_body, subject=subject)
    mail.send(message)

def cancellation_emails(reservations):
    # receives a list of reservation objects
    movie_name = reservations[0].projection.movie.name
    movie_projection_date = str(reservations[0].projection.date)
    info = [(reservation.user.email, reservation.user.name, str(reservation.seats), str(reservation.date)) for reservation in reservations]
    for email, name, seats, date in info:
        subject = "Reservation made in " + str(date) + "has been cancelled"
        msg_body = "Hello " + name + "\nSadly a projection in which you had made a reservation has been cancelled.\nDetails\n\tMovie name: " + movie_name + "\n\tMovie date: " + movie_projection_date + "\n\tSeats: " + str(seats)
        message = Message( recipients=[email], body=msg_body, subject=subject)
        mail.send(message)
"""
