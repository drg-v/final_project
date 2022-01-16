from flask import Blueprint
from flask_restful import Api

teams = Blueprint('teams', __name__)
teams_api = Api(teams)

from . import teams
from . import team
