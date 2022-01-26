"""
Module containing restful resource for users in general

Classes:
    Users(Resource)
"""

from flask_restful import Resource, fields, marshal_with
from service import user_service
from utils import admin_token_required
from . import users_api

user_fields = {
    'users': fields.List(fields.Nested({
        'id_': fields.Integer,
        'username': fields.String,
        'status': fields.String,
        'is_subscriber': fields.Boolean,
        'trial_attempts': fields.Integer,
        'is_admin': fields.Boolean
    }))
}


class Users(Resource):
    """
    A class used to represent Users resource

    Methods
    _______
    get()
        returns all users from the database
    """

    @staticmethod
    @admin_token_required
    @marshal_with(user_fields)
    def get():
        """Processes get request and returns all users"""

        return {'users': user_service.get_all_users()}, 200


users_api.add_resource(Users, '')
