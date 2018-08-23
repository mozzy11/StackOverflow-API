import unittest
import json
from app.views.view import app
from app.models.questions  import  Questions

class Test_Case(unittest.TestCase):


        hostname = 'http://localhost:5000/api/v1/questions/1'
        null_qtn_host = 'http://localhost:5000/api/v1/questions/4'

        app = app.test_client()
        app.testing = True
        question = {
            'qtn_id': 1,
            'qtn_body': 'what is Andela',
            'user_id': 1
        }

        qtnobj = Questions()
        qtnobj.set_qtn(1, "what is Andela", 1 )



        def test_wrong_method(self):

           res = self.app.post(self.hostname, data = self.question )
           self.assertEqual(res.status_code, 405)

        def test_get_qtn(self):

           respon = self.app.get(self.hostname)
           self.assertTrue(respon.status_code == 200)


        def test_get_ryt_response(self):

            respon = self.app.get(self.hostname)
            self.assertIn('what is Andela', str(respon.data))

        def test_get_ryt_response(self):

            respon = self.app.get(self. null_qtn_host)
            self.assertIn('Please Request usng an Existing Question id', str(respon.data))


if __name__ == "__main__":
    unittest.main()