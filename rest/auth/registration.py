from flask_restful import Resource, fields, marshal_with, reqparse
from service import user_service
from . import auth_api


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'username', dest='username',
    location='json', required=True,
    help='The user\'s username',
)

post_parser.add_argument(
    'password', dest='password',
    location='json',
    required=True, help='The user\'s email',
)

registration_fields = {
    'status': fields.String,
}


class Registration(Resource):

    @marshal_with(registration_fields)
    def post(self):
        args = post_parser.parse_args()
        result = user_service.create_user(args.username, args.password)
        res = {'status': result}, 200 if result == 'success' else 400
        return res


auth_api.add_resource(Registration, '/register')
