# app.py
def add(a, b):
    return a - b  # Bug: Should be a + b

# test_app.py
import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5) # This will fail
