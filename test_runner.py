import unittest, os
from scrabble_tests import test_api, test_app, test_classes

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(test_api))
suite.addTests(loader.loadTestsFromModule(test_app))
suite.addTests(loader.loadTestsFromModule(test_classes))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

