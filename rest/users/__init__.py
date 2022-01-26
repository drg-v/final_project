"""
Package containing users blueprint and restful resources

Modules:
    user.py : contains resource for single user
    users.py : contains resource for users in general
Variables:
    users_bp : Blueprint
"""

from flask import Blueprint
from flask_restful import Api

users_bp = Blueprint('users_bp', __name__)
users_api = Api(users_bp)

from . import user
from . import users
