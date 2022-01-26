"""
Module containing tests for teams

Functions:
    test_get_teams(client, token)
    test_post_team(client, token)
    test_post_team_fail(client, token)
    test_put_team(client, token)
    test_put_team_fail(client, token)
"""

import json


def test_get_teams(client, token):
    """Get all teams success test"""

    response = client.get('teams', headers={"Content-Type": "application/json",
                                            "Authorization": "Bearer " + token})
    assert 200 == response.status_code
    assert 2 == len(response.json['teams'])


def test_post_team(client, token):
    """Post team success test"""

    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'losses': 2,
                          'value': 878000000,
                          'points': 43})
    response = client.post('teams',
                           headers={"Content-Type": "application/json",
                                    "Authorization": "Bearer " + token},
                           data=payload)
    assert 200 == response.status_code
    assert "success" == response.json['status']


def test_post_team_fail(client, token):
    """Post team fail test"""

    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'value': 878000000,
                          'points': 43})
    response = client.post('teams',
                           headers={"Content-Type": "application/json",
                                    "Authorization": "Bearer " + token},
                           data=payload)
    assert 400 == response.status_code


def test_put_team(client, token):
    """Put team success test"""

    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'losses': 2,
                          'value': 878000000,
                          'points': 43})
    response = client.put('teams/2',
                          headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer " + token},
                          data=payload)
    assert 200 == response.status_code
    assert "success" == response.json['status']


def test_put_team_fail(client, token):
    """Put team fail test"""

    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'losses': 2,
                          'value': 878000000,
                          'points': 43})
    response = client.put('teams/10',
                          headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer " + token},
                          data=payload)
    assert 401 == response.status_code
    assert 'fail' == response.json['status']
