import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    DEBUG = True
    TESTING = False

    MONGODB_SETTINGS = {
        'db': str(os.environ.get('MONGODB_DB')),
        'host': str(os.environ.get('MONGODB_HOST')),
        'port': int(os.environ.get('MONGODB_PORT'))
    }


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    # TODO: mock mongodb
    TESTING = True
