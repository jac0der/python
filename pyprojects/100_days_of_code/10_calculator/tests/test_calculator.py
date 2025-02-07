import unittest
from calculator.calculator import calculate, get_number, get_operation

class TestCalculator(unittest.TestCase):

    def test_calculate_valid_inputs(self):         
        self.assertEqual(calculate(6.0, 2.0, '/'), 3.0)


if __name__ == '__main__':
    unittest.main()