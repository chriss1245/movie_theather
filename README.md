# A cinema web page 🐍
A full web server of a cinema running in python


<div>
 <img width="430" src="https://user-images.githubusercontent.com/58918297/146336799-cebdd684-fb83-499b-8da9-801bf06be035.png">
 <img width="450" src="https://user-images.githubusercontent.com/58918297/146341776-35330f90-58dc-4c31-a9d1-ea9a9b8109cc.png">
</div>

### Backend technologies
 - python
 - flask framework 
 - sql-alchemy
 - mariadb

### Frontend technologies
 - html
 - css
 - javascript
 
### Folder structure
```
movie_theather
   ├── __init__.py
   ├── main.py: genemovie_theatherral controller
   ├── data.py: our rest api for asking data 
   ├── auth.py: controllers spetialized in login management
   ├── model.py: will contain the database structure we have
   ├── analytics.py: methods for NLP sentiment analysis of site reviews and average movie ratings, generation of encoded pie chart and bar plot to be shown in  administrator view
   ├── utils.py: contain some functions needed but not quite realted
   ├── flask_init.sh & flask_init.ps1: exports the needed environment variables for running flask, we still     need to execute flask run
   ├── .gitignore: list with files we do not want to be at the repository
   ├── requirements.txt: list of all the dependencies (python -m pip install -r requirements.txt: automates the install of these dependencies)
   ├── documentation
   │    └── all the manuals and stuff to take into account
   ├── static
   │    ├── css files
   │    ├──img
   │    |  └── all the images we will need for the movies
   │    └── js
   │         └── js files
   ├──templates
   │    ├──main
   │    |    └── all the views we are going to show
   │    └── src
   │         └── html files that can be included or inherited for our main views
   └── src
         └── Where our user`s profile image are stored
```

### Functionalities

#### Main page:
- Slider with the best rated movies
- Search bar with a button to sort movies based on an specific criteria
- Cards with the movies and their data

#### User page
* Profile picture (
* customer 
* administrator
### Additional functionalities implemented
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


