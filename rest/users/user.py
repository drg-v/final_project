from flask_restful import Resource, fields, marshal_with, reqparse
from service import user_service
from utils import admin_token_required
from . import users_api


get_parser = reqparse.RequestParser()
get_parser.add_argument(
    'all', dest='all',
    location='json', required=True,
    help='The user\'s username',
)
get_parser.add_argument(
    'username', dest='username',
    location='json', required=False,
    help='The user\'s username',
)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'status': fields.String,
    'is_subscriber': fields.Boolean,
    'trial_attempts': fields.Integer,
    'is_admin': fields.Boolean
}

patch_parser = reqparse.RequestParser()
patch_parser.add_argument(
    'username', dest='username',
    location='json', required=True,
    help='The user\'s username',
)
patch_parser.add_argument(
    'operation', dest='operation',
    location='json', required=True,
    help='User operation',
)

patch_fields = {
    'operation': fields.String,
    'status': fields.String
}


class User(Resource):

    @admin_token_required
    @marshal_with(user_fields)
    def get(self):
        return user_service.get_all_users()

    @admin_token_required
    @marshal_with(patch_fields)
    def patch(self):
        args = patch_parser.parse_args()
        if args.operation == 'subscribe':
            res = user_service.add_user_subscription(args.username)
        else:
            res = user_service.block_user(args.username)
        code = 200 if res == 'success' else 401
        return {'operation': args.operation, 'status': res}, code


users_api.add_resource(User, '/')
