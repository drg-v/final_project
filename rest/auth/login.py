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

login_fields = {
    'status': fields.String,
    'token': fields.String,
    'user': fields.Nested({
        'id': fields.Integer,
        'username': fields.String,
        'status': fields.String,
        'is_subscriber': fields.Boolean,
        'trial_attempts': fields.Integer,
        'is_admin': fields.Boolean
    })
}


class Login(Resource):

    @marshal_with(login_fields)
    def post(self):
        args = post_parser.parse_args()
        result = user_service.login_user(args.username, args.password)
        if result:
            token, user = result
            print("AFTER SERVICE", token, user.username)
            res = {'status': 'success', 'token': token, 'user': user}, 200
        else:
            res = {'status': 'fail'}, 401
        return res


auth_api.add_resource(Login, '/login')
