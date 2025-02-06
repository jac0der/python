from leap.leap_year import is_leap_year
from leap.leap_error import LeapYearError
import unittest

class TesLeapYear(unittest.TestCase):
    def test_leap_years(self):
        """Test known leap years."""
        self.assertTrue(is_leap_year(2000))  # Divisible by 400
        self.assertTrue(is_leap_year(2024))  # Divisible by 4, but not 100
        self.assertTrue(is_leap_year(2400))  # Divisible by 400

    def test_non_leap_years(self):
        """Test known non-leap years."""
        self.assertFalse(is_leap_year(1900))  # Divisible by 100, but not 400
        self.assertFalse(is_leap_year(2023))  # Not divisible by 4
        self.assertFalse(is_leap_year(2100))  # Divisible by 100, but not 400

    def test_invalid_input(self):
        """Test invalid inputs raising LeapYearError."""
        with self.assertRaises(LeapYearError) as contex:            
            is_leap_year("2024")  # String input
        with self.assertRaises(LeapYearError):
            is_leap_year(2024.5)  # Float input
        with self.assertRaises(LeapYearError):
            is_leap_year(None)  # None input
        with self.assertRaises(LeapYearError):
            is_leap_year([])  # List input


if __name__ == "__main__":
    unittest.main()
