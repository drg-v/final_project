"""
Module containing restful resource for matches

Classes:
    Matches(Resource)
"""

from flask_restful import Resource, reqparse
from service import match_service
from utils import admin_token_required
from . import matches_api

post_parser = reqparse.RequestParser()

post_parser.add_argument(
    'home_id', dest='home_id',
    location='json', required=True,
    help='Home_id',
)

post_parser.add_argument(
    'away_id', dest='away_id',
    location='json', required=True,
    help='Away_id',
)

post_parser.add_argument(
    'match_date', dest='match_date',
    location='json', required=True,
    help='Match_date',
)


class Matches(Resource):
    """
    A class used to represent Matches resource

    Methods
    _______
    post()
        Returns the result of adding a new match
    """

    @staticmethod
    @admin_token_required
    def post():
        """
        Processes adding match attempt and returns the result

        :return: the status of adding attempt
        """

        args = post_parser.parse_args()
        result = match_service.add_match(args)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


matches_api.add_resource(Matches, '')
