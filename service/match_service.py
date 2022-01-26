"""
Module containing functions to work with Match model

Functions:
    get_all_matches() -> List[Match]
    get_matches(team_id: int) -> List[Match]
    get_by_range(team_id: int, start: datetime, end: datetime) -> List[Match]
    get_match(match_id: int) -> Match
    add_match(data: Namespace) -> str
    delete_match(match_id: int) -> str
"""

from argparse import Namespace
from typing import List
from datetime import datetime

from models.models import Match, Team
from app import db
from service import team_service


def get_all_matches() -> List[Match]:
    """Returns all matches"""

    return Match.query.all()


def get_matches(team_id: int) -> List[Match]:
    """Returns all matches for the appropriate team"""

    team = team_service.get_team(team_id)
    return team.matches if team else None


def get_by_range(team_id: int, start: datetime, end: datetime) -> List[Match]:
    """
    Returns all matches between 2 dates for appropriate team

    :param team_id: team id
    :param start: date representing start of time range
    :param end: date representing end of time range
    :return: a list of matches
    """

    return Match.query.join(Match.teams) \
        .filter(Team.id_ == team_id, start <= Match.date, Match.date <= end) \
        .all()


def get_match(match_id: int) -> Match:
    """Returns the match with appropriate id_"""

    return Match.query.filter_by(id_=match_id).first()


def add_match(data: Namespace) -> str:
    """
    Creates new Match entity if data is valid and returns 'success',
    otherwise returns 'fail'

    :param data: Namespace containing match values
    :return: the status of adding attempt
    """

    home = team_service.get_team(data.home_id)
    away = team_service.get_team(data.away_id)
    if not (home and away):
        return 'fail'
    match_date = datetime.strptime(data.match_date, '%Y-%b-%d %H:%M:%S')
    match = Match(date=match_date)
    home.matches.append(match)
    away.matches.append(match)
    db.session.commit()
    return 'success'


def delete_match(match_id: int) -> str:
    """
    Deletes match with appropriate match_id if it exists

    :param match_id: match id
    :return: the status of deleting attempt
    """

    match = Match.query.filter_by(id_=match_id).first()
    if not match:
        return 'fail'
    db.session.delete(match)
    db.session.commit()
    return 'success'
