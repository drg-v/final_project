from models.models import Match
from app import db
from service import team_service
from datetime import datetime


def get_all_matches():
    return Match.query.all()


def get_matches(team_id):
    team = team_service.get_team(team_id)
    return team.matches if team else None


def get_match(match_id):
    return Match.query.filter_by(id_=match_id).first()


def add_match(data):
    home = team_service.get_team(data.home_id)
    away = team_service.get_team(data.away_id)
    if not (home and away):
        return 'fail'
    match_date = datetime.strptime(data.match_date, '%Y-%m-%d %H:%M:%S')
    match = Match(date=match_date)
    home.matches.append(match)
    away.matches.append(match)
    db.session.commit()
    return 'success'


def delete_match(match_id):
    match = Match.query.filter_by(id_=match_id).first()
    if not match:
        return 'fail'
    db.session.delete(match)
    db.session.commit()
    return 'success'
