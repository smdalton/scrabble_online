import unittest
import app
from copy import deepcopy
import json

BASE_URL = 'http://127.0.0.1:5000/'
routes = ['debug','','is-valid-word', 'reset-bag', 'test','get-hand' ]
class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_response_code_all_routes(self):
        for route in routes:
            response = self.app.get(BASE_URL+route)
            self.assertEqual(response.status_code, 200, route)

    def test_default_route(self):
        response = self.app.get(BASE_URL)
        print(response.data)

    def test_is_valid_word(self):
        word = 'cheeseburger'
        response = self.app.get(BASE_URL+'is-valid-word'+'?check-word='+word)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['check-word'], word, data)
        self.assertEqual(data['valid'], 'true', data)

    # test debug route that dumps the internal state of the server
    def test_reset_bag(self):
        initial_bag_response = self.app.get(BASE_URL+'debug')
        reset_bag_response = self.app.get(BASE_URL+'reset-bag'+'?test=true')
        initial_state_data = json.loads(initial_bag_response.get_data(as_text=True))
        reset_bag_data = json.loads(reset_bag_response.get_data(as_text=True))
        # check that the old board is the same as current board from the point in time before
        self.assertEqual(initial_state_data['current-bag'], reset_bag_data['old-board'])
        # test multiple routes with this one
        self.assertNotEqual(reset_bag_data['old-board'], reset_bag_data['new-board'])


    def test_fail(self):
        print('continue testing here')
        self.assertEqual(1,1, 'continue the testing')