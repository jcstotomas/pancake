import os 


class Config:
    FLASK_APP = "run.py"
    SECRET_KEY = "howdy"
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    print(SQLALCHEMY_DATABASE_URI)
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:memsjeremy@localhost/pancake'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig:
    DEBUG = True
