from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__, static_folder='/static')
    app.config.from_object(config)
    CORS(app)
    Api(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from rest.auth import auth
    from rest.teams import teams
    from rest.matches import matches_bp
    from rest.users import users
    from rest.predictions import predictions

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(teams, url_prefix='/teams')
    app.register_blueprint(matches_bp)
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(predictions, url_prefix='/predictions')
    return app


if __name__ == "__main__":
    app = create_app('config.ProdConfig')
    app.run("0.0.0.0", debug=True)
