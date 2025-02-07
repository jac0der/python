import unittest
from calculator.calculator import calculate, get_number, get_operation

class TestCalculator(unittest.TestCase):

    def test_calculate_valid_inputs(self):         
        self.assertEqual(calculate(6.0, 2.0, '/'), 3.0)
        self.assertEqual(calculate(3.0, 2.4, '/'), 1.25)
        
        self.assertEqual(calculate(100.3375, 2.733, '*'), 274.22)
        self.assertEqual(calculate(94.95, 67.89, '*'), 6446.16)

        self.assertEqual(calculate(-7.0, 2.0, '+'), -5.0)
        self.assertEqual(calculate(-8.0, -2.4, '+'), -10.4)

        self.assertEqual(calculate(7.3, 8.9, '-'), -1.6)
        self.assertEqual(calculate(33.33, 4.0, '-'), 29.33)


if __name__ == '__main__':
    unittest.main()