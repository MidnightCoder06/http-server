# cd tests
# python -m unittest test_method_handlers

import unittest
import test_utils
import sys
sys.path.append('../src/utils')
sys.path.append('../src/model')
import exceptions
import repository
import method_handlers

'''
self.assertEqual(method_name, 'PUT ', 'method name does not match')
assertIn(a, b)   a in b
# need to know how to check for custom errors ->  assertRaises()
# assertRaises(exception, *, msg=None)
'''

class TestMethodHandlers(unittest.TestCase):
    def setUp(self):
        self.storage = repository.Repository().data

    def tearDown(self):
        self.storage = None

    def test_put_create_route(self):
        pass

    def test_put_update_route(self):
        pass

    def test_get_existing_route(self):
        pass

    def test_get_nonexistant_route(self):
        pass

    def test_delete_existing_route(self):
        pass

    def test_delete_nonexistant_route(self):
        pass
