from flask_restful import Resource, fields, marshal_with, reqparse
from service import user_service
from utils import admin_token_required
from . import users_api

user_fields = {
    'users': fields.List(fields.Nested({
        'id': fields.Integer,
        'username': fields.String,
        'status': fields.String,
        'is_subscriber': fields.Boolean,
        'trial_attempts': fields.Integer,
        'is_admin': fields.Boolean
    }))
}


class Users(Resource):

    @admin_token_required
    @marshal_with(user_fields)
    def get(self):
        return {'users': user_service.get_all_users()}, 200


users_api.add_resource(Users, '')
