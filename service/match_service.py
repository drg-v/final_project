from models.models import Match
from app import db
from service import team_service


def get_all_matches():
    return Match.query.all()


def get_matches(team_id):
    print("match_team_id: ", team_id)
    return team_service.get_team(team_id).matches


def get_match(match_id):
    return Match.query.filter_by(id_=match_id).first()


def add_match(data):
    match = Match(date=data.match_date)
    print(match)
    print("MATCH TEAMS", match.teams)
    home = team_service.get_team(data.home_id)
    away = team_service.get_team(data.away_id)
    match.teams.extend((home, away))
    db.session.commit()
    print("AFTER COMMIT")
    return 'success'


def delete_match(match_id):
    match = Match.query.filter_by(id_=match_id).first()
    if not match:
        return 'fail'
    db.session.delete(match)
    db.session.commit()
    return 'success'
