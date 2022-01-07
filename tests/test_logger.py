# cd tests
# python -m unittest test_logger

import unittest
import sys
sys.path.append('../src/logger')
import logger
import test_utils


class TestLogger(unittest.TestCase):
    # The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method
    def setUp(self):
        # includes database initialization
        self.logger = logger.Logger()

    # provide a tearDown() method that tidies up after the test method has been run
    def tearDown(self):
        '''
        The dispose method provides a way to explicitly release the Python object represented by a PyObject instance. It is a good idea to call Dispose on PyObjects that wrap resources that are limited or need strict lifetime control. Otherwise, references to Python objects will not be released until a managed garbage collection occurs.
        '''
        self.logger.destory_logs()

    def test_logger(self):
        self.logger.log(test_utils.mock_update_arg)
        method_name = self.logger.logs[0].values()[0]['method_name']
        path = self.logger.logs[0].values()[0]['path']
        self.assertEqual(method_name, 'PUT ', 'method name does not match')
        self.assertEqual(path, '{repository}', 'path does not match')
