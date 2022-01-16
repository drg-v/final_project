from flask_restful import Resource, fields, marshal_with
from service import team_service
from utils import token_required
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


class Teams(Resource):

    @token_required
    @marshal_with(teams_fields)
    def get(self):
        return {'teams': team_service.get_all_teams()}, 200


teams_api.add_resource(Teams, '/')
