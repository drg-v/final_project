"""
Module containing restful resource for single team

Classes:
    Team(Resource)
"""

from flask_restful import Resource, fields, marshal_with, reqparse
from service import team_service
from utils import token_required, admin_token_required
from . import teams_api


put_parser = reqparse.RequestParser()
put_parser.add_argument(
    'name', dest='name',
    location='json', required=True,
    help='Team name',
)
put_parser.add_argument(
    'goals_for', dest='goals_for',
    location='json', required=True,
    help='Team goals_for', type=int
)
put_parser.add_argument(
    'goals_against', dest='goals_against',
    location='json', required=True,
    help='Team goals_against', type=int
)
put_parser.add_argument(
    'wins', dest='wins',
    location='json', required=True,
    help='Team wins', type=int
)
put_parser.add_argument(
    'losses', dest='losses',
    location='json', required=True,
    help='Team losses', type=int
)
put_parser.add_argument(
    'value', dest='value',
    location='json', required=True,
    help='Team value', type=int
)
put_parser.add_argument(
    'points', dest='points',
    location='json', required=True,
    help='Team points', type=int
)

put_fields = {
    'status': fields.String
}

team_fields = {
        'id_': fields.Integer,
        'name': fields.String,
        'goals_for': fields.String,
        'goals_against': fields.String,
        'wins': fields.Integer,
        'losses': fields.Integer,
        'value': fields.Integer,
        'points': fields.Integer
}

delete_fields = put_fields


class Team(Resource):
    """
    A class used to represent Team resource

    Methods
    _______
    get(id_: int)
        Returns team with appropriate id_ if it exists
    put(id_: int)
        Returns the result of changing the team with appropriate id_
   delete(id_: int)
        Returns the result of deleting the team with appropriate id_
    """

    @staticmethod
    @token_required
    @marshal_with(team_fields)
    def get(id_: int):
        """
        Processes get request for the team with appropriate id_ and
        returns the result if the team exists.

        :param id_: team id
        :return: team if it exists
        """

        result = team_service.get_team(id_)
        code = 200 if result else 401
        return {'team': result}, code

    @staticmethod
    @admin_token_required
    @marshal_with(put_fields)
    def put(id_: int):
        """
        Processes updating attempt for the team with appropriate id_
        and returns the result

        :param id_: team id
        :return: the status of updating attempt
        """

        args = put_parser.parse_args()
        result = team_service.change_team(id_, args)
        code = 200 if result == 'success' else 401
        return {'status': result}, code

    @staticmethod
    @admin_token_required
    @marshal_with(delete_fields)
    def delete(id_: int):
        """
        Processes deleting attempt for the team with appropriate id_
        and returns the result

        :param id_: team id
        :return: the status of deleting attempt
        """

        result = team_service.delete_team(id_)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


teams_api.add_resource(Team, '/<int:id_>')
