"""
Module containing restful resource for registration

Classes:
    Registration(Resource)
"""

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
    """
    A class used to represent Registration resource

    Methods
    _______
    post()
        Returns the result of registration attempt
    """

    @staticmethod
    @marshal_with(registration_fields)
    def post():
        """
        Processes registration attempt and returns the result

        :return: status of registration attempt
        """

        args = post_parser.parse_args()
        result = user_service.create_user(args.username, args.password)
        res = {'status': result}, 200 if result == 'success' else 400
        return res


auth_api.add_resource(Registration, '/register')
