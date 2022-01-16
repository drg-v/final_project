from flask import Blueprint
from flask_restful import Api

matches_bp = Blueprint('matches_bp', __name__)
matches_api = Api(matches_bp)

from . import match
from . import match_post
