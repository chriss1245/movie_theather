from flask import Flask
from flask_sqlalchemy  import SQLAlchemy



db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"

    # SQL ALCHEMY
    """
    app.config["SQLALCHEMY_DATABASE_URI"] =\
        "mysql+mysqldb://22_appweb_20:ch2663s7@mysql.lab.it.uc3m.es/22_appweb_20b"
    """
    app.config['SQLALCHEMY_DATABASE_URI']=\
        "mysql://chris:yolo@localhost/theather"
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 'False'
    db.init_app(app)
    
    #BLUEPRINTS
    from . import main, data
    app.register_blueprint(main.bp)
    app.register_blueprint(data.bp)
    
    return app
