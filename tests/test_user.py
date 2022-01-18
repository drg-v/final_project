import json


def test_get_users(client, token):
    response = client.get('users',
                          headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                   })
    assert 200 == response.status_code
    assert 1 == len(response.json)


def test_subscribe_user(client, token):
    payload = json.dumps({'operation': 'subscribe'})
    response = client.patch('users/1',
                            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                     }, data=payload)
    assert 200 == response.status_code
    assert "subscribe" == response.json['operation']
    assert "success" == response.json['status']


def test_subscribe_user_fail(client, token):
    payload = json.dumps({'operation': 'subscribe'})
    response = client.patch('users/10',
                            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                     }, data=payload)
    assert 401 == response.status_code
    assert "subscribe" == response.json['operation']
    assert "fail" == response.json['status']


def test_block_user(client, token):
    payload = json.dumps({'operation': 'block'})
    response = client.patch('users/1',
                            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                     }, data=payload)
    assert 200 == response.status_code
    assert "block" == response.json['operation']
    assert "success" == response.json['status']


def test_block_user_fail(client, token):
    payload = json.dumps({'operation': 'block'})
    response = client.patch('users/10',
                            headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                     }, data=payload)
    assert 401 == response.status_code
    assert "block" == response.json['operation']
    assert "fail" == response.json['status']
