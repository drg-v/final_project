import json

from tests import BaseCase


class TestPrediction(BaseCase):

    def test_get_prediction(self):

        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjQ0Njk5MjgxLCJhZG0iOnRydWV9.gf3Fs2VdwsuGSPJSHebbgnR4JGtN8nPICW58ddWMuJY"
        response = self.app.get('predict/1', headers={"Content-Type": "application/json", "Authorization": "Bearer " + token
                                                  })
        print("RESPONSE DATA: ", response.data)
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response.json['home'], float)
        self.assertIsInstance(response.json['away'], float)
        self.assertIsInstance(response.json['draw'], float)
        