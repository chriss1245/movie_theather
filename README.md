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

<b>movie_theather</b>
    - __init__.py
    - mian.py: general controller
    - data.py: our rest api for asking data 
    - model.py: will contain the database structure we have
    - analytics.py: File with methods of AI for analytics
    - utils.py: contain some functions needed but not quite realted
    - flask_init.sh & flask_init.ps1: exports the needed environment variables for running flask, we still     need to execute flask run
    - .gitignore: list with files we do not want to be at the repository
    - requirements.txt: list of all the dependencies (python -m pip install -r requirements.txt: automates the install of these dependencies)
    <b>documentation</b>
        - all the manuals and stuff to take into account
    <b>static</b>
        - css files
        <b>img</b>
            - all the images we will need
        <b>js</b>
            - js files
    <b>templates</b>
        <b>main</b>
            - all the views we are going to show
        <b>src</b>
            - html files that can be included or inherited for our main views


   