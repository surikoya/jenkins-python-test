import pytest

from basic import hello

class HelloWorldTest(unittest.TestCase):

    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!")
