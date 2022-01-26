"""
Package containing teams blueprint and restful resources

Modules:
    team.py : contains resource for single team
    teams.py : contains resource for teams in general
Variables:
    teams_bp : Blueprint
"""

from flask import Blueprint
from flask_restful import Api

teams_bp = Blueprint('teams_bp', __name__)
teams_api = Api(teams_bp)

from . import teams
from . import team
