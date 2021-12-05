from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_seasurf import SeaSurf
from flask_talisman import Talisman





def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    #csrf = CSRFProtect(app)
    from . import main, data
    app.register_blueprint(main.bp)
    app.register_blueprint(data.bp)
    csrf = SeaSurf(app)
    # content secure policy directives
    csp = {
        'default-src': '\'self\'',
        'img-src':'*'
    }

    # disables access to geolocation interface
    feature_policy = {
        'geolocation': '\'none\''
    }

    talisman = Talisman(app, content_security_policy=csp, feature_policy=feature_policy)
    return app
