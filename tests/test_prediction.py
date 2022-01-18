def test_get_prediction(client, token):
    response = client.get('predictions/1',
                          headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                   })
    assert 200 == response.status_code
    assert isinstance(response.json['home'], float)
    assert isinstance(response.json['away'], float)
    assert isinstance(response.json['draw'], float)


def test_get_prediction_fail(client, token):
    response = client.get('predictions/10',
                          headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                   })
    assert 401 == response.status_code
    assert 'fail' == response.json['status']
