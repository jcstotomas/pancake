
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


def hello_world():
    return "Hello world"

db = SQLAlchemy()

from .database.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    migrate = Migrate(app,db)
    from app.route_handlers import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v0.1')
    with app.app_context():
        db.create_all()
    return app

