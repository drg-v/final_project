from flask_restful import Resource, fields, marshal_with, reqparse
from service import match_service
from flask import jsonify
from utils import token_required, admin_token_required
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


class MatchPost(Resource):

    @admin_token_required
    def post(self):
        print("HERE PLS")
        args = post_parser.parse_args()
        print(args)
        result = match_service.add_match(args)
        code = 200 if result == 'success' else 401
        print("BEFORE RETURN")
        return {'status': result}, code


matches_api.add_resource(MatchPost, '/matches')
