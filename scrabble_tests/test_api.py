import unittest
import app
from copy import deepcopy
import json

BASE_URL = 'http://127.0.0.1:5000/'
routes = ['debug', ]
class ApiTestCase(unittest.TestCase):

    def setUp(self):
        print('in test_api')
        self.app = app.app.test_client()
        self.app.testing = True

    def test_response_code_alll_routes(self):
        routes = ['debug', ]

        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_fail(self):
        self.assertEqual(1,1, 'test called successfully')