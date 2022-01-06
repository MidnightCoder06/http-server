# cd tests
# python -m test_logger
'''
You can pass in a list with any combination of module names, and fully qualified class or method names.

Test modules can be specified by file path as well:

python -m unittest tests/test_something.py
'''

import unittest
import sys
sys.path.append('../src/logger')
import logger
import logs_database


class TestLogger(unittest.TestCase):
    # The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method
    def setUp(self):
        # database initialization
        #self.database = logs_database.LogsDatabase()
        pass

    # provide a tearDown() method that tidies up after the test method has been run
    def tearDown(self):
        '''
        The dispose method provides a way to explicitly release the Python object represented by a PyObject instance. It is a good idea to call Dispose on PyObjects that wrap resources that are limited or need strict lifetime control. Otherwise, references to Python objects will not be released until a managed garbage collection occurs.
        '''
        #self.database.dispose()
        pass

    def test_logger(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        pass

'''

import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')


'''
