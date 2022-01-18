import json


def test_login(client):
    """User registration and login test"""
    username = "dsl"
    password = "sld"
    payload = json.dumps({
        "username": username,
        "password": password
    })
    response = client.post('auth/register', headers={"Content-Type": "application/json"}, data=payload)
    assert response.json['status'] == 'success'
    assert 200 == response.status_code
    response = client.post('auth/login', headers={"Content-Type": "application/json"}, data=payload)
    assert isinstance(response.json['token'], str)
    assert response.json['status'] == 'success'
    assert 200 == response.status_code


def test_login_fail(client):
    """User registration and login test"""
    username = "dsl"
    password = "sld"
    payload = json.dumps({
        "username": username,
        "password": password
    })
    response = client.post('auth/login', headers={"Content-Type": "application/json"}, data=payload)
    assert response.json['status'] == 'fail'
    assert 401 == response.status_code
