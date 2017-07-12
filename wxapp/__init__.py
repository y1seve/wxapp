from flask import Flask
from webapp.models import db

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name) 

    db.init_app(app)

    @app.route('/')
    def index():
        return 'hello, world'

        
    return app
