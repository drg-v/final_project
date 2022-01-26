"""
Module containing functions to work with Team model

Functions:
    get_all_teams() -> List[Team]
    get_team(team_id: int) -> Team
    add_team(data: Namespace) -> str
    change_team(team_id: int, data: Namespace) -> str
    delete_team(team_id: int) -> str
"""

from argparse import Namespace
from typing import List

from models.models import Team
from app import db


def get_all_teams() -> List[Team]:
    """Returns all teams from the database"""

    return Team.query.all()


def get_team(team_id: int) -> Team:
    """Returns the team with appropriate id_"""

    return Team.query.filter_by(id_=team_id).first()


def add_team(data: Namespace) -> str:
    """
    Creates the team if in not exists

    :param data: Namespace containing team fields
    :return: the status of the team creation attempt
    """

    team = Team.query.filter_by(name=data.name).first()
    if not team:
        team = Team(name=data.name,
                    goals_for=data.goals_for,
                    goals_against=data.goals_against,
                    wins=data.wins,
                    losses=data.losses,
                    value=data.value,
                    points=data.points)
        db.session.add(team)
        db.session.commit()
        return 'success'
    return 'fail'


def change_team(team_id: int, data: Namespace) -> str:
    """
    Changes the team with appropriate team_id

    :param team_id: team id
    :param data: Namespace containing team fields
    :return: the status of changing attempt
    """

    team = Team.query.filter_by(id_=team_id).first()
    if not team:
        return 'fail'
    team.name = data.name
    team.goals_for = data.goals_for
    team.goals_against = data.goals_against
    team.wins = data.wins
    team.losses = data.losses
    team.value = data.value
    team.points = data.points
    db.session.commit()
    return 'success'


def delete_team(team_id: int) -> str:
    """Deletes the team with appropriate id_ if it exists"""

    team = Team.query.filter_by(id_=team_id).first()
    if not team:
        return 'fail'
    db.session.delete(team)
    db.session.commit()
    return 'success'
