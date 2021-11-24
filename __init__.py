from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

from textblob import TextBlob

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"

    from . import main, data
    app.register_blueprint(main.bp)
    app.register_blueprint(data.bp)
    
    return app
