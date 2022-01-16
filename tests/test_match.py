import json

from tests import BaseCase


class TestMatch(BaseCase):

    def test_get_matches(self):

        payload = json.dumps({
            "team_id": 1,
        })

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.get('match', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  }, data=payload)
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(18, len(response.json['matches']))
        self.assertEqual(2, len(response.json['matches'][0]['teams']))

    def test_post_match(self):

        payload = json.dumps({
            "home_id": 1,
            "away_id": 2,
            "match_date": "2021-06-12 09:55:22"
        })

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.post('match', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  }, data=payload)
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual('success', response.json['status'])

    def test_delete_match(self):

        payload = json.dumps({
            "match_id": 15
        })

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.delete('match', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  }, data=payload)
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual('success', response.json['status'])
