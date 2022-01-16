from models.models import Team
from app import db


def get_all_teams():
    return Team.query.all()


def get_team(team_id):
    return Team.query.filter_by(id_=team_id).first()


def add_team(data):
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


def change_team(data):
    team = Team.query.filter_by(id_=data.id_).first()
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

