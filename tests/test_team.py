import json

from tests import BaseCase


class TestTeam(BaseCase):

    def test_get_teams(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.get('teams', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  })
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.json['teams']))

    def test_post_team(self):
        payload = json.dumps({'name': "Chelsea",
                              'goals_for': 45,
                              'goals_against': 16,
                              'wins': 12,
                              'losses': 2,
                              'value': 878000000,
                              'points': 43})

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.post('teams', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  }, data=payload)
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json['status'])

    def test_put_team(self):
        payload = json.dumps({'name': "Chelsea",
                              'goals_for': 45,
                              'goals_against': 16,
                              'wins': 12,
                              'losses': 2,
                              'value': 878000000,
                              'points': 43})

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.put('teams', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  }, data=payload)
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json['status'])
