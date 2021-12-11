from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_talisman import Talisman
from flask_seasurf import SeaSurf
from flask_mail import Mail

mail = Mail()
csrf = SeaSurf()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    from . import main, data
    app.register_blueprint(main.bp)
    app.register_blueprint(data.bp)

    # content secure policy directives
    csp = {
        'default-src': '*',
        'img-src':'*',
        'script-src':'\'self\''

    }

    # disables access to geolocation interface, and disables microphone

    feature_policy = {
        'geolocation': '\'none\'',
        'microphone': '()'
    }

    talisman = Talisman(app, content_security_policy=csp, feature_policy=feature_policy, content_security_policy_nonce_in=['script-src'])
    # Flask mail
    mail.init_app(app)
    app.conf["MAIL_USERNAME"] = "CinemaCarlosiii@gmail.com"
    app.conf["MAIL_PASSWORD"] = "ProyectoWebApps"
    # # Seasurf
    csrf.init_app(app)
    return app
