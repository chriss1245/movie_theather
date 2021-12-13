# A cinema web page


A full web server running in python.

## Backend technologies
 - flask framework
 - sql-alchemy
 - mariadb.

## Frontend technologies
 - html
 - css
 - javascript
 
### Folder structure

movie_theather

    - __init__.py
    - main.py: general controller
    - data.py: our rest api for asking data 
    - model.py: will contain the database structure we have
    - analytics.py: methods for NLP sentiment analysis of site reviews and average movie ratings, generation of encoded pie chart and bar plot
    to be shown in administrator view
    - utils.py: contain some functions needed but not quite realted
    - flask_init.sh & flask_init.ps1: exports the needed environment variables for running flask, we still     need to execute flask run
    - .gitignore: list with files we do not want to be at the repository
    - requirements.txt: list of all the dependencies (python -m pip install -r requirements.txt: automates the install of these dependencies)
    documentation
        - all the manuals and stuff to take into account
    static
        - css files
        img
            - all the images we will need
        js
            - js files
    templates
        main
            - all the views we are going to show
        src
            - html files that can be included or inherited for our main views


### Additional functionalities implemented
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

From a security stand point:
 - Included flask_talisman wrapper to ensure security that fits the needs of the webpage, control security protocols only allows upload of images from any origin, we also disallow the usage of the microphone and geolocation among other things. We kept the HTTP  headers kept with default options. Reference: https://github.com/wntrblm/flask-talisman/blob/main/README.rst
 - Included flask_seasurf library to protect against cross-site request forgery.

Reservation-wise:
 - Email with reservation details as soon as it is made
 - When a projection is cancelled, all the users with reservations on it are notified automatically through cancellation emails.


