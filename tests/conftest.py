import pytest
from app import create_app
from app import db
from models.models import User, Team, Match
from werkzeug.security import generate_password_hash
import json
import datetime


def init_test_db(database):
    database.drop_all()
    database.create_all()
    password = generate_password_hash('test_password')
    user = User(username='test_user',
                password=password,
                status='active',
                is_subscriber=False,
                trial_attempts=2,
                is_admin=True)
    database.session.add(user)
    team = Team(name='Liverpool',
                goals_for=55,
                goals_against=18,
                wins=13,
                losses=2,
                value=861000000,
                points=45)
    database.session.add(team)
    team_2 = Team(name='Man City',
                  goals_for=54,
                  goals_against=13,
                  wins=18,
                  losses=2,
                  value=1040000000,
                  points=56)
    match = Match(date=datetime.datetime.now())
    team.matches.append(match)
    team_2.matches.append(match)
    database.session.add(team_2)
    database.session.commit()


@pytest.fixture
def client():
    """Pytest fixture to configure app test client"""
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            init_test_db(db)
        yield client


@pytest.fixture
def token(client):
    username = 'test_user'
    password = 'test_password'
    payload = json.dumps({
        "username": username,
        "password": password
    })
    response = client.post('auth/login', headers={"Content-Type": "application/json"}, data=payload)
    return response.json['token']
