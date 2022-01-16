from flask_restful import Resource, fields, marshal_with, reqparse
from service import prediction_service
from utils import token_required, admin_token_required
from . import predictions_api

prediction_fields = {
    'status': fields.String,
    'home': fields.Float,
    'away': fields.Float,
    'draw': fields.Float
}


class Prediction(Resource):

    @token_required
    @marshal_with(prediction_fields)
    def get(self, id_):
        result = prediction_service.get_prediction(id_)
        if result == 'fail':
            return {'status': 'fail'}, 401
        return {'home': result[0][0],
                'away': result[0][1],
                'draw': result[0][2],
                'status': 'success'
                }, 200


predictions_api.add_resource(Prediction, '/<int:id_>')
