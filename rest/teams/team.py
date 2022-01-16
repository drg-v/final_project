from flask_restful import Resource, fields, marshal_with, reqparse
from service import team_service
from utils import token_required, admin_token_required
from . import teams_api


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

put_parser = post_parser.copy()

put_parser.add_argument(
    'id_', dest='id_',
    location='json', required=True,
    help='Team id', type=int
)

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


class Team(Resource):

    @token_required
    @marshal_with(team_fields)
    def get(self, id_):
        return {'team': team_service.get_team(id_)}, 200

    @admin_token_required
    @marshal_with(post_fields)
    def post(self):
        args = post_parser.parse_args()
        result = team_service.add_team(args)
        return {'status': result}, 200 if result == "success" else {'status': result}, 401

    @admin_token_required
    @marshal_with(post_fields)
    def put(self):
        args = put_parser.parse_args()
        result = team_service.change_team(args)
        return {'status': result}, 200 if result == "success" else {'status': result}, 401


teams_api.add_resource(Team, '/<int:id>')
