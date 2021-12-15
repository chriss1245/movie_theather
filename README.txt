Participants
    - Christopher André Manzano Vimos -
    - Jorge Parreño Hernández - 100429982
    - Marco Narganes Fraile - 100428692


Additional functionalities implemented
From the main page:
    - Search bar
    - Button to sort movies based on an specific criteria
    - Navigation Bar
From customer view:

    -Display of profile picture and user information.
    -Button to cancel reservations.
    -Ability for users to write site reviews.

From Administrator view:
    - Pie chart in which the amount of neutral, positive and negative reviews is shown, using NLP, passed as a base64 encoded version of the graph generated in matplotlib
    - Bar plot of the average ratings of each movie, given by the users, sorted from best to worst.
    - Bar plots representing the amount of taken and available seats per existing projection.
    - Projection views for all existing projections with an individual graph to represent the taken and available seats.
    - Inside projection views, we allow for cancellation of particular customer reservation and a textarea input to send as a cancellation email.

From a security stand point:
    - Included flask_talisman extension to ensure security that fits the needs of the webpage, control security protocols only allows upload of images from any origin, we also disallow the usage of the microphone and geolocation among other things. We kept the HTTP headers kept with default options. Reference: https://github.com/wntrblm/flask-talisman/blob/main/README.rst
    - Included flask_seasurf library to protect against cross-site request forgery. Reference:https://flask-seasurf.readthedocs.io/en/latest/

Reservation-wise:
    - Email with reservation details as soon as it is made
    - When a projection is cancelled, all the users with reservations on it are notified automatically through cancellation emails.