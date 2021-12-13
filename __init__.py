from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from flask_seasurf import SeaSurf
from flask_talisman import Talisman

db = SQLAlchemy()
bcrypt = Bcrypt()
csrf = SeaSurf()
talisman = Talisman()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"

    #LOGIN MANAGER
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from . import model
    @login_manager.user_loader
    def load_user(user_id):
        return model.User.query.get(int(user_id))
    
    # SQL ALCHEMY
    
    app.config["SQLALCHEMY_DATABASE_URI"] =\
        "mysql+mysqldb://22_appweb_20:ch2663s7@mysql.lab.it.uc3m.es/22_appweb_20c"
    """
    app.config['SQLALCHEMY_DATABASE_URI']=\
        "mysql://chris:yolo@localhost/theather"
    """
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 'False'
    db.init_app(app)
    
    #BLUEPRINTS
    from . import main, data, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(data.bp)
    app.register_blueprint(auth.bp)

    #SEASURF
    csrf.init_app(app)
    
    #TALISMAN
    csp = {
        'default-src': '*',
        'img-src':['*', 'data:'],
        'script-src':'\'self\'',
    }

    # disables access to geolocation interface, and disables microphone

    feature_policy = {
        'geolocation': '\'none\'',
        'microphone': '()'
    }
    talisman.init_app(app, content_security_policy=csp, feature_policy=feature_policy)

    return app
