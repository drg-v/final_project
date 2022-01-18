from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import get_config


db = SQLAlchemy()
migrate = Migrate()
cors = CORS()


def create_app(config):
    app = Flask(__name__, static_folder='/static')
    app.config.from_object(get_config(config))
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

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


if __name__ == "__main__":
    app = create_app('production')
    app.run("0.0.0.0", debug=True)
