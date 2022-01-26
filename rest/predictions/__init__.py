"""
Package containing predictions blueprint and restful resource

Modules:
    prediction.py : contains resource for prediction
Variables:
    predictions_bp : Blueprint
"""

from flask import Blueprint
from flask_restful import Api

predictions_bp = Blueprint('predictions_bp', __name__)
predictions_api = Api(predictions_bp)

from . import prediction
