from flask import Blueprint
from flask_restful import Api

predictions = Blueprint('predictions', __name__)
predictions_api = Api(predictions)

from . import prediction
