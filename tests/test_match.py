import json


def test_post_match(client, token):
    payload = json.dumps({
        "home_id": 1,
        "away_id": 2,
        "match_date": "2020-Jun-12 09:55:22"
    })
    response = client.post('matches', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                               }, data=payload)
    assert 200 == response.status_code
    assert 'success' == response.json['status']


def test_post_match_fail(client, token):
    payload = json.dumps({
        "home_id": 1,
        "away_id": 10,
        "match_date": "2020-06-12 09:55:22"
    })
    response = client.post('matches', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                               }, data=payload)
    assert 401 == response.status_code
    assert 'fail' == response.json['status']


def test_get_matches(client, token):
    response = client.get('matches/1', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                })
    assert 200 == response.status_code
    assert 1 == len(response.json['matches'])
    assert 2 == len(response.json['matches'][0]['teams'])


def test_get_matches_fail(client, token):
    response = client.get('matches/10', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                 })
    assert 401 == response.status_code


def test_delete_match(client, token):
    response = client.delete('matches/1',
                             headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                      })
    assert 200 == response.status_code
    assert 'success' == response.json['status']


def test_delete_match_fail(client, token):
    response = client.delete('matches/10',
                             headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                      })
    assert 401 == response.status_code
    assert 'fail' == response.json['status']


def test_get_matches_by_range(client, token):
    url = 'matches/1?startDate=2000-Jun-12 09:55:22&endDate=2040-Jun-12 09:55:22'
    response = client.get(url, headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                 })
    assert 200 == response.status_code
    assert 1 == len(response.json['matches'])
    assert 2 == len(response.json['matches'][0]['teams'])
