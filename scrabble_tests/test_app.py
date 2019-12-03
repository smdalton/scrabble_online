import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        print('in test_app')
