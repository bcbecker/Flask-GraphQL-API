from flask_mongoengine import MongoEngine
from flask import Flask
from config import Config


db = MongoEngine()


def create_app(config_class=Config):
    '''
    Binds all necessary objects to app instance, registers blueprints, configs from .env
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Bind any packages here
    db.init_app(app)

    # Register any blueprints here
    from .routes import employees
    app.register_blueprint(employees)

    return app
