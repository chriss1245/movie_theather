# A cinema web page


<img width="800" src="https://github-readme-stats.vercel.app/api/pin/?username=chriss1245&repo=movie_theather&theme=vue-dark" align="center"/>
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
 - Display of profile picture and user information
 - Button to cancel reservations 
 - Ability for users to write site reviews

From Administrator view:
 - Pie chart in which the amount of neutral, positive and negative reviews is shown, using NLP, passed as a base64 encoded version

From a security stand point:
 - Added Jinja directive to prevent cross-site scripting

   
