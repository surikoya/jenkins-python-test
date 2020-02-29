import unittest
import sys
sys.path.append('./src')

import hello

class HelloWorldTest(unittest.TestCase):

    def test_say_hi(self):
        self.assertEqual(hello.hello(), "Hello, World!")
