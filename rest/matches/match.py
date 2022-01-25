from flask_restful import Resource, fields, marshal_with
from datetime import datetime
from service import match_service
from flask import request
from utils import token_required, admin_token_required
from . import matches_api

get_fields = {
    'matches': fields.List(fields.Nested({
        'id_': fields.Integer,
        'date': fields.DateTime,
        'teams': fields.List(fields.Nested({
            'id_': fields.Integer,
            'name': fields.String,
        }))
    })
    )
}


class Match(Resource):

    @token_required
    @marshal_with(get_fields)
    def get(self, id_):
        start = request.args.get('startDate')
        end = request.args.get('endDate')
        if start and end:
            start_date = datetime.strptime(start, '%Y-%b-%d %H:%M:%S')
            end_date = datetime.strptime(end, '%Y-%b-%d %H:%M:%S')
            result = match_service.get_matches_by_range(id_, start_date, end_date)
        else:
            result = match_service.get_matches(id_)
        code = 200 if result else 401
        return {'matches': result}, code

    @admin_token_required
    def delete(self, id_):
        result = match_service.delete_match(id_)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


matches_api.add_resource(Match, '/<int:id_>')
