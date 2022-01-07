# cd tests
# python -m unittest test_method_handlers

import unittest
import test_utils
import sys
sys.path.append('../src/model')
import repository
import method_handlers


class TestMethodHandlers(unittest.TestCase):
    # this setUp and tearDown is just for example purposes. the database can't be accessed like this
    def setUp(self):
        self.repo = repository.Repository()
        self.storage = self.repo.data

    def tearDown(self):
        self.storage = self.repo.delete_repository()

    def test_put_create_route(self):
        method_handlers.create_item(test_utils.mock_put_arg)

    def test_put_update_route(self):
        method_handlers.update_item(test_utils.mock_update_arg)

    def test_get_existing_route(self):
        # with self.assertRaises(exceptions.PathNotStored) as exception_context:
        #     method_handlers.read_item(test_utils.mock_get_arg)
        method_handlers.read_item(test_utils.mock_get_arg, True)

    def test_get_nonexistant_route(self):
        method_handlers.read_item(test_utils.mock_get_arg, True)

    def test_delete_existing_route(self):
        method_handlers.delete(test_utils.mock_delete_arg, True)

    def test_delete_nonexistant_route(self):
        method_handlers.delete(test_utils.mock_delete_arg, True)
        # need to know how to check for custom errors ->  assertRaises()
        # assertRaises(exception, *, msg=None)
