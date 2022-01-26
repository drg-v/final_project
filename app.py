"""
Module containing flask application factory and db instance

Functions:
    create_app(config)

Variables:
    db : SQLAlchemy()
"""

import logging
import sys
from flask import Flask
from flask.logging import create_logger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import get_config


db = SQLAlchemy()
migrate = Migrate()
cors = CORS()


def create_app(config):
    """
    Flask application factory

    :param config: str representing app config
    :return: flask app
    """

    app = Flask(__name__, static_folder='/static')
    app.config.from_object(get_config(config))
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

    file_handler = logging.FileHandler(filename='app.log', mode='w')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    logger = create_logger(app)
    logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.handlers.clear()
    werkzeug_logger.addHandler(file_handler)
    werkzeug_logger.addHandler(console_handler)
    werkzeug_logger.setLevel(logging.DEBUG)

    from rest.auth import auth
    from rest.teams import teams_bp
    from rest.matches import matches_bp
    from rest.users import users_bp
    from rest.predictions import predictions_bp

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(teams_bp, url_prefix='/teams')
    app.register_blueprint(matches_bp, url_prefix='/matches')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(predictions_bp, url_prefix='/predictions')
    return app
