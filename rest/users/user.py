from flask_restful import Resource, fields, marshal_with, reqparse
from service import user_service
from utils import admin_token_required
from . import users_api

patch_parser = reqparse.RequestParser()
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
    @marshal_with(patch_fields)
    def patch(self, id_):
        args = patch_parser.parse_args()
        if args.operation == 'subscribe':
            res = user_service.add_user_subscription(id_)
        else:
            res = user_service.block_user(id_)
        code = 200 if res == 'success' else 401
        return {'operation': args.operation, 'status': res}, code


users_api.add_resource(User, '/<int:id_>')
