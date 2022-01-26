"""
Module containing restful resource for prediction

Classes:
    Prediction(Resource)
"""

from flask_restful import Resource, fields, marshal_with
from service import prediction_service
from utils import token_required
from . import predictions_api

prediction_fields = {
    'status': fields.String,
    'home': fields.Float,
    'away': fields.Float,
    'draw': fields.Float
}


class Prediction(Resource):
    """
    A class used to represent Prediction resource

    Methods
    _______
    get(id_: int)
        Returns prediction of the match if it exists, otherwise fail
    """

    @staticmethod
    @token_required
    @marshal_with(prediction_fields)
    def get(id_: int):
        """
        Processes prediction attempt for the team with appropriate id_
        and returns the result if it exists

        :param id_: match id
        :return: prediction status and result
        """

        result = prediction_service.get_prediction(id_)
        if result == 'fail':
            return {'status': 'fail'}, 401
        return {'home': result[0],
                'away': result[1],
                'draw': result[2],
                'status': 'success'
                }, 200


predictions_api.add_resource(Prediction, '/<int:id_>')
