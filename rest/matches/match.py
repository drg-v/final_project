from flask_restful import Resource, fields, marshal_with, reqparse
from service import match_service
from utils import token_required, admin_token_required
from . import matches_api

get_fields = {
    'matches': fields.List(fields.Nested({
        'id': fields.Integer,
        'date': fields.DateTime,
        'teams': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String,
        }))
    })
    )
}


class Match(Resource):

    @token_required
    @marshal_with(get_fields)
    def get(self, id_):
        result = match_service.get_matches(id_)
        code = 200 if result else 401
        return {'matches': result}, code

    @admin_token_required
    def delete(self, id_):
        result = match_service.delete_match(id_)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


matches_api.add_resource(Match, '/<int:id_>')
