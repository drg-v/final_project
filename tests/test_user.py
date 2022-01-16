import json

from tests import BaseCase


class TestUser(BaseCase):

    def test_get_users(self):

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.get('user',
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                          })
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json))

    def test_subscribe_user(self):
        payload = json.dumps({'username': 'dsl', 'operation': 'subscribe'})

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.patch('user',
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                          }, data=payload)
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("subscribe", response.json['operation'])
        self.assertEqual("success", response.json['status'])
