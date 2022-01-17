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

    @token_required
    @marshal_with(team_fields)
    def get(self, id_):
        result = team_service.get_team(id_)
        code = 200 if result else 401
        return {'team': result}, code

    @admin_token_required
    @marshal_with(put_fields)
    def put(self, id_):
        args = put_parser.parse_args()
        result = team_service.change_team(id_, args)
        code = 200 if result == 'success' else 401
        return {'status': result}, code

    @admin_token_required
    @marshal_with(delete_fields)
    def delete(self, id_):
        result = team_service.delete_team(id_)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


teams_api.add_resource(Team, '/<int:id_>')
