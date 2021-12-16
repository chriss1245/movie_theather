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
* Profile picture (can be changed)
* ##### Customer
   * View of all the reservations done for already seen and not seen projections
   * The future projections can be cancelled
   * Can give feedback of the website
   * <img height=300 src=https://user-images.githubusercontent.com/58918297/146429223-a34254ea-62cd-46cb-a89e-d492530472cb.png>
* ##### Administrator
   * Plots of analytics: (reviews piechart, movie ranking barplot & projections' crew status barplot)  
   * View of all the projections that are programmed
   * Chance to cancel projections (if there are reservations done. The user associated to those reservations will recieve an email)
     <div>
      <img width=400 height=300 src="https://user-images.githubusercontent.com/58918297/146430767-bb4fbdb5-e0b7-43e3-a579-6d5ca4374f66.png">
      <img width=400 height=300 src="https://user-images.githubusercontent.com/58918297/146430775-6987cf2b-b173-4bca-a3e3-b1b3e822e70c.png">
      <img width=400  src="https://user-images.githubusercontent.com/58918297/146430822-6cad17c6-253b-4794-bad4-44fae59d3028.png">
     </div>
   * Projection view (enables view and cancel individual reservations)
   * <img width=400 height=300 src="https://user-images.githubusercontent.com/58918297/146432729-5fa6f5ca-71f3-4e3c-a188-f6eccbb982dd.png">
* #### Movie
  *  Trailer of the movie
  *  Rating
  *  Enables rating the movie
  *  ![movie](https://user-images.githubusercontent.com/58918297/146433072-1206807e-e545-4abe-9839-e2df7d4af8b6.png)
* #### Reservation
  * Shows all the projections in the given week (can move among weeks)
  * ![reservation](https://user-images.githubusercontent.com/58918297/146433234-fc8c4db6-6d79-4927-9dd9-1d39792fe99c.gif)
  * The user will recieve a confirmation email
  * ![email_reservation](https://user-images.githubusercontent.com/58918297/146433646-4289aebf-1895-4bbc-b46c-9f28937c6931.png)

 
* #### Security:
  * Included flask_talisman extension to ensure security that fits the needs of the webpage, control security protocols only allows upload of images from any origin, we also disallow the usage of the microphone and geolocation among other things. We kept the HTTP  headers kept with default options. Reference:  https://github.com/wntrblm/flask-talisman/blob/main/README.rst
  *  Included flask_seasurf library to protect against cross-site request forgery. Reference: https://flask-seasurf.readthedocs.io/en/latest/
 
