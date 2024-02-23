from unittest.mock import MagicMock
import unittest

from foo import Foo

class TestFoo(unittest.TestCase):
    
    def setUp(self):
        self.foo = Foo()
        self.mockFoo = Foo()
        self.mockFoo.doo = MagicMock(return_value='mocked_foo')
        
    
    def test_doo(self):
        self.assertEqual('doo', self.foo.doo())

    def test_mock_doo(self):
        self.assertEqual('mocked_foo', self.mockFoo.doo())
    
