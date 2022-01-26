"""
Package containing auth blueprint and restful resources

Modules:
    login.py : contains login resource
    registration.py : contains registration resource
Variables:
    auth : Blueprint
"""

from flask import Blueprint
from flask_restful import Api

auth = Blueprint('auth', __name__)
auth_api = Api(auth)

from . import registration
from . import login
