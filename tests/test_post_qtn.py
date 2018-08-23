import unittest
import json
from app.views.view import app

class Test_Case(unittest.TestCase):


        hostname = 'http://localhost:5000/api/v1/questions'
        invalid_host_name = 'http://localhost:5000/api/v1'

        app = app.test_client()
        app.testing = True

        qtn = {
            "qtn_id": 2,
            "qtn_body": "what is a boot camp",
            "user_id": 2
            }

        invalid_qtn = {
            "ans_id": 2000,
            "ans_content": "A boot Camp is a two weeks training for a new Intake",
        }

        empty = {}


        def test_ryt_response(self):
           respon = self.app.post(self.hostname , data = json.dumps(self.qtn ),content_type='application/json',)
           assert respon.status_code == 200

        def test_invalid_qtn(self):
            respon = self.app.post(self.hostname, data = json.dumps(self. invalid_qtn),content_type='application/json',)
            self.assertFalse(respon.status_code == 200)

        def test_get_ryt_response(self):
            respon = self.app.post(self.hostname,  data = json.dumps(self.qtn ),content_type='application/json',)
            self.assertIn('what is a boot camp', str(respon.data))

        def test_empty_qtn(self):
            respon = self.app.post(self.hostname, data=json.dumps(self.empty ), content_type='application/json', )
            self.assertIn('Invalid Qtn', str(respon.data))



if __name__ == "__main__":
    unittest.main()