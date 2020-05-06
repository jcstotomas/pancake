
from flask import Flask
def hello_world():
    return "Hello world"



def create_app():
    app = Flask(__name__)

    @app.route('/')    
    def hello():
        return "Hey"

    return app