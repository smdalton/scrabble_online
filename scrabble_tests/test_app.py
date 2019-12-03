import unittest
from app import app

#Integration test module

class AppTestCase(unittest.TestCase):
    def setUp(self):
        print('in test_app')
