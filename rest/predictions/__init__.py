from flask import Blueprint
from flask_restful import Api

predictions_bp = Blueprint('predictions_bp', __name__)
predictions_api = Api(predictions_bp)

from . import prediction
