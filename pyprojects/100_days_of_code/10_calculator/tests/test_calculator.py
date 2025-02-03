import unittest
from calculator.calculator import calculate, get_number, get_operation

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(10, 5, '+'), 15)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 5, '-'), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(10, 5, '*'), 50)

    def test_division(self):
        self.assertEqual(calculate(10, 5, '/'), 2)

    def test_division_by_zero(self):
        self.assertIsNone(calculate(10, 0, '/'))

    def test_invalid_operation(self):
        self.assertIsNone(calculate(10, 5, '%'))
       

if __name__ == '__main__':
    unittest.main()