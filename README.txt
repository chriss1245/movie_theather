PARTICIPANTS
    - Christopher André Manzano Vimos - 100429927
    - Jorge Parreño Hernández - 100429982
    - Marco Narganes Fraile - 100428692

USER if teacher wants to try it:
    -User: yolo@yolo.com 
    -Password: yolo

ADITIONAL FUNCTIONALITIES IMPLEMENTED

The additional functionalities were implemented throughout various parts of the web server, for each of the sections we performed the following:
From the main page:
 - Search bar
 - Button to sort movies based on an specific criteria
 - Navigation Bar

From customer view:
 - Display of profile picture and user information.
 - Button to cancel reservations. 
 - Ability for users to write site reviews.

From Administrator view:
 - Pie chart in which the amount of neutral, positive and negative reviews is shown, using NLP, passed as a base64 encoded version of the graph generated in matplotlib
 - Bar plot of the average ratings of each movie, given by the users, sorted from best to worst.
 - Bar plots representing the amount of taken and available seats per existing projection, in which at least one seat is not available for reservation.
 
Projection view
 - Accessed only by administrators, we display all the reservations made on a given projection, with data to identify the users, from which we see a button to cancel the whole projection, in the same manner as from the administrator view, and a button to cancel reservations of a particular user, sending a custom body for the cancellation email.
 - We display a stacked bar chart in which we see the amount of taken and available seats for the given projection.

From a security stand point:
 - Included flask_talisman extension to ensure security that fits the needs of the webpage, control security protocols only allows upload of images from any origin, we also disallow the usage of the microphone and geolocation among other things. We kept the HTTP  headers kept with default options. Reference: https://github.com/wntrblm/flask-talisman/blob/main/README.rst
 - Included flask_seasurf library to protect against cross-site request forgery. Reference:https://flask-seasurf.readthedocs.io/en/latest/
 
Reservation-wise:
 - Email with reservation details as soon as it is made.
 - When a projection is cancelled, all the users with reservations on it are notified automatically through cancellation emails.
