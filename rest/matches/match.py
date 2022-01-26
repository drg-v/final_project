"""
Module containing restful resource for single match

Classes:
    Match(Resource)
"""

from datetime import datetime
from flask_restful import Resource, fields, marshal_with
from flask import request
from service import match_service
from utils import token_required, admin_token_required
from . import matches_api

get_fields = {
    'matches': fields.List(fields.Nested({
        'id_': fields.Integer,
        'date': fields.DateTime,
        'teams': fields.List(fields.Nested({
            'id_': fields.Integer,
            'name': fields.String,
        }))
    })
    )
}


class Match(Resource):
    """
    A class used to represent Match resource

    Methods
    _______
    get(id_: int)
        Returns all matches for team with id_. Can take optional
        url parameters and return matches between 2 dates.
    delete(id_: int)
        Returns the result of delete attempt of the team with id_.
    """

    @staticmethod
    @token_required
    @marshal_with(get_fields)
    def get(id_: int):
        """
        Returns all matches for the team with appropriate id_

        There are two optional parameters: startDate and EndDate.
        If they are present it returns all matches between these
        two dates.

        :param id_: team id
        :return: a list of matches
        """

        start = request.args.get('startDate')
        end = request.args.get('endDate')
        if start and end:
            start_date = datetime.strptime(start, '%Y-%b-%d %H:%M:%S')
            end_date = datetime.strptime(end, '%Y-%b-%d %H:%M:%S')
            result = match_service.get_by_range(id_, start_date, end_date)
        else:
            result = match_service.get_matches(id_)
        code = 200 if result else 401
        return {'matches': result}, code

    @staticmethod
    @admin_token_required
    def delete(id_: int):
        """
        Returns the result of deleting match with appropriate id_
        if it exists.

        :param id_: match id
        :return: the status of deleting attempt
        """

        result = match_service.delete_match(id_)
        code = 200 if result == 'success' else 401
        return {'status': result}, code


matches_api.add_resource(Match, '/<int:id_>')
