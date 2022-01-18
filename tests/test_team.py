import json


def test_get_teams(client, token):
    response = client.get('teams', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                            })
    assert 200 == response.status_code
    assert 2 == len(response.json['teams'])


def test_post_team(client, token):
    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'losses': 2,
                          'value': 878000000,
                          'points': 43})
    response = client.post('teams', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                               }, data=payload)
    assert 200 == response.status_code
    assert "success" == response.json['status']


def test_post_team_fail(client, token):
    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'value': 878000000,
                          'points': 43})
    response = client.post('teams', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                               }, data=payload)
    assert 400 == response.status_code


def test_put_team(client, token):
    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'losses': 2,
                          'value': 878000000,
                          'points': 43})
    response = client.put('teams/2', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                              }, data=payload)
    assert 200 == response.status_code
    assert "success" == response.json['status']


def test_put_team_fail(client, token):
    payload = json.dumps({'name': "Chelsea",
                          'goals_for': 45,
                          'goals_against': 16,
                          'wins': 12,
                          'losses': 2,
                          'value': 878000000,
                          'points': 43})
    response = client.put('teams/10', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                              }, data=payload)
    assert 401 == response.status_code
    assert 'fail' == response.json['status']
