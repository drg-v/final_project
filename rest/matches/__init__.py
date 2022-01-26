"""
Package containing matches blueprint and restful resources

Modules:
    match.py : contains resource for single match
    matches.py : contains resource for matches in general
Variables:
    matches_bp : Blueprint
"""

from flask import Blueprint
from flask_restful import Api

matches_bp = Blueprint('matches_bp', __name__)
matches_api = Api(matches_bp)

from . import match
from . import matches
