# cd tests
# python -m unittest test_request_response

import unittest
import test_utils


class TestRequestResponse(unittest.TestCase):
    def test_created(self):
        self.assertEqual(utils.say_hello("Geekflare"), "Hello, Geekflare")

    def test_ok(self):
        pass

    def test_delete(self):
        pass

    def test_not_found(self):
        pass
