# cd tests
# python -m unittest test_request_response

import unittest
import sys
sys.path.append('../src/view')
import request_response


class TestRequestResponse(unittest.TestCase):
    def setUp(self):
        self.view = request_response.View()

    def test_created(self):
        response = self.view.created('mock route')
        self.assertIn('Status', response)
        self.assertEqual(response['Status'], '201 Created')
        self.assertIn('oid', response)

    def test_ok(self):
        response = self.view.ok()
        self.assertIn('Status', response)
        self.assertEqual(response['Status'], '200 OK')
        self.assertIn('oid', response)


    def test_delete(self):
        actual = self.view.delete()
        expected = {'Status': '200 OK'}
        self.assertEqual(actual, expected)

    def test_not_found(self):
        actual = self.view.not_found()
        expected = {'Status': '404 Not Found'}
        self.assertEqual(actual, expected)
