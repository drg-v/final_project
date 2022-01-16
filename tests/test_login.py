import json


def test_login(client):
    username = "dsl"
    password = "sld"
    payload = json.dumps({
        "username": username,
        "password": password
    })
    response = client.post('auth/register', headers={"Content-Type": "application/json"}, data=payload)
    print("RESPONSE 1: ", response)
    # When
    response = client.post('auth/login', headers={"Content-Type": "application/json"}, data=payload)

    # Then
    assert isinstance(response.json['token'], str)
    assert 200 == response.status_code
