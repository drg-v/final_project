"""
Module containing restful resource for teams in general

Classes:
    Teams(Resource)
"""

from flask_restful import Resource, fields, marshal_with, reqparse
from service import team_service
from utils import token_required, admin_token_required
from . import teams_api

teams_fields = {
    'teams': fields.List(fields.Nested({
        'id_': fields.Integer,
        'name': fields.String,
        'goals_for': fields.String,
        'goals_against': fields.String,
        'wins': fields.Integer,
        'losses': fields.Integer,
        'value': fields.Integer,
        'points': fields.Integer}))
}

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'name', dest='name',
    location='json', required=True,
    help='Team name',
)
post_parser.add_argument(
    'goals_for', dest='goals_for',
    location='json', required=True,
    help='Team goals_for', type=int
)
post_parser.add_argument(
    'goals_against', dest='goals_against',
    location='json', required=True,
    help='Team goals_against', type=int
)
post_parser.add_argument(
    'wins', dest='wins',
    location='json', required=True,
    help='Team wins', type=int
)
post_parser.add_argument(
    'losses', dest='losses',
    location='json', required=True,
    help='Team losses', type=int
)
post_parser.add_argument(
    'value', dest='value',
    location='json', required=True,
    help='Team value', type=int
)
post_parser.add_argument(
    'points', dest='points',
    location='json', required=True,
    help='Team points', type=int
)

post_fields = {
    'status': fields.String
}


class Teams(Resource):
    """
    A class used to represent Teams resource

    Methods
    _______
    get()
        Returns all teams from the database
    post()
        Returns the result of adding new team
    """

    @staticmethod
    @token_required
    @marshal_with(teams_fields)
    def get():
        """Returns all teams from the database"""

        return {'teams': team_service.get_all_teams()}, 200

    @staticmethod
    @admin_token_required
    @marshal_with(post_fields)
    def post():
        """
        Processes adding the new team attempt and returns the result

        :return: the status of adding attempt
        """

        args = post_parser.parse_args()
        result = team_service.add_team(args)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


teams_api.add_resource(Teams, '')
