"""
Module containing tests for users

Functions:
    test_get_users(client, token)
    test_subscribe_user(client, token)
    test_subscribe_user_fail(client, token)
    test_block_user(client, token)
    test_block_user_fail(client, token)
"""

import json


def test_get_users(client, token):
    """Get all users success test"""

    response = client.get('users',
                          headers={"Content-Type": "application/json",
                                   "Authorization": "Bearer " + token})
    assert 200 == response.status_code
    assert 1 == len(response.json)


def test_subscribe_user(client, token):
    """Subscribe user success test"""

    payload = json.dumps({'operation': 'subscribe'})
    response = client.patch('users/1',
                            headers={"Content-Type": "application/json",
                                     "Authorization": "Bearer " + token},
                            data=payload)
    assert 200 == response.status_code
    assert "subscribe" == response.json['operation']
    assert "success" == response.json['status']


def test_subscribe_user_fail(client, token):
    """Subscribe user fail test"""

    payload = json.dumps({'operation': 'subscribe'})
    response = client.patch('users/10',
                            headers={"Content-Type": "application/json",
                                     "Authorization": "Bearer " + token},
                            data=payload)
    assert 401 == response.status_code
    assert "subscribe" == response.json['operation']
    assert "fail" == response.json['status']


def test_block_user(client, token):
    """Block user success test"""

    payload = json.dumps({'operation': 'block'})
    response = client.patch('users/1',
                            headers={"Content-Type": "application/json",
                                     "Authorization": "Bearer " + token},
                            data=payload)
    assert 200 == response.status_code
    assert "block" == response.json['operation']
    assert "success" == response.json['status']


def test_block_user_fail(client, token):
    """Block user fail test"""

    payload = json.dumps({'operation': 'block'})
    response = client.patch('users/10',
                            headers={"Content-Type": "application/json",
                                     "Authorization": "Bearer " + token},
                            data=payload)
    assert 401 == response.status_code
    assert "block" == response.json['operation']
    assert "fail" == response.json['status']
