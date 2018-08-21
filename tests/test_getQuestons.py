import unittest
import json
from app.views.vew import app

class Test_Case(unittest.TestCase):


        hostname = 'http://localhost:5000/api/v1/questions'

        app = app.test_client()
        app.testing = True
        question = {
            'qtn_id': 1,
            'qtn_body': 'what is Andela',
            'User_id': 1
        }


        def test_wrong_method(self):
           res = self.app.post(self.hostname, data = self.question )
           self.assertEqual(res.status_code, 405)

        def test_get_qtn(self):
           respon = self.app.get(self.hostname)
           assert respon.status_code == 200


        def test_get_ryt_response(self):
            respon = self.app.get(self.hostname)
            self.assertIn('what is Andela', str(respon.data))

if __name__ == "__main__":
    unittest.main()