import unittest
import json
from app.views.view import app

class Test_Case(unittest.TestCase):


        hostname = 'http://localhost:5000/api/v1/questions/1/answers'
        null_qtn_host = 'http://localhost:5000/api/v1/questions/2/answers'

        app = app.test_client()
        app.testing = True

        ans ={
            "ans_id": 1,
            "ans_content": "A boot Camp is a two weeks training for a new Intake",
            "qtn_id": 2014
        }

        invalid_ans = {
            "ans_id": 2000,
            "ans_content": "A boot Camp is a two weeks training for a new Intake",
        }



        def test_wrong_method(self):
           res = self.app.get(self.hostname, data = json.dumps(self.ans ))
           self.assertEqual(res.status_code, 405)

        def test_get_qtn(self):
           respon = self.app.post(self.hostname , data = json.dumps(self.ans ),content_type='application/json',)
           assert respon.status_code == 200

        def test_invalidans(self):
            respon = self.app.post(self.hostname, data = json.dumps(self.invalid_ans),content_type='application/json',)
            self.assertFalse(respon.status_code == 200)

        def test_nullqtn(self):
            respon = self.app.post(self.null_qtn_host, data = json.dumps(self.ans))
            self.assertFalse(respon.status_code == 200)


        def test_correct (self):
            respon = self.app.post(self.hostname, data= json.dumps(self.ans),content_type='application/json',)
            data = json.loads(respon.get_data(as_text=True))
            assert data['ans_id'] == 1


if __name__ == "__main__":
    unittest.main()