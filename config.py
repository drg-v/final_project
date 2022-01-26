"""
Module containing flask configuration classes and function

Classes:
    Config
    ProdConfig(Config)
    TestConfig(Config)

Functions:
    get_config(config: str) -> Config

"""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """
    A class used to represent basic app config

    Attributes
    __________
    SECRET_KEY : str
        a secret key for password hashing
    SQLALCHEMY_TRACK_MODIFICATIONS : boolean
        indicates SQLAlchemy track modifications
    STATIC_FOLDER : str
        a path for static folder
    """

    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = 'static'


class ProdConfig(Config):
    """
    A class used to represent production config

    Attributes
    __________
    FLASK_ENV : str
        used to indicate flask environment
    DEBUG : boolean
        indicates flask debug mode
    TESTING : boolean
        indicates flask testing mode
    SQLALCHEMY_DATABASE_URI : str
        uri to connect to the database
    """

    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class TestConfig(Config):
    """
        A class used to represent testing config

        Attributes
        __________
        FLASK_ENV : str
            used to indicate flask environment
        DEBUG : boolean
            indicates flask debug mode
        TESTING : boolean
            indicates flask testing mode
        SQLALCHEMY_DATABASE_URI : str
            uri to connect to the database
        """

    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')


configs = {
    'testing': TestConfig,
    'production': ProdConfig
}


def get_config(config: str) -> Config:
    """A utility function used to get config class by string name"""

    return configs.get(config, ProdConfig)
