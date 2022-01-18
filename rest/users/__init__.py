from flask import Blueprint
from flask_restful import Api

users_bp = Blueprint('users_bp', __name__)
users_api = Api(users_bp)

from . import user
from . import users
