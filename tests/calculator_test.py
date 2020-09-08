import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))
    
    def test_subtract(self):
        expected = 2
        self.assertEqual(expected, subtract(20, 18))
    
    def test_divide(self):
        expected = 4
        self.assertEqual(expected, divide(48, 12))
    
    def test_multiply(self):
        self.assertEqual(360, multiply(20, 18))


    pass
