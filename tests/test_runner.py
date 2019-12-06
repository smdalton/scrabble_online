import unittest, os
from tests import test_api, test_app, test_classes, test_dictionary

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(test_api))
suite.addTests(loader.loadTestsFromModule(test_app))
suite.addTests(loader.loadTestsFromModule(test_classes))
suite.addTests(loader.loadTestsFromModule(test_dictionary))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)


# for clean coverage report
# coverage run --source . test_runner.py


