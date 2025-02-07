import unittest
from unittest.mock import patch
from leap.leap_year import is_leap_year, get_year, exit_program
from leap.leap_error import LeapYearError

class TestLeapYear(unittest.TestCase):

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
        with self.assertRaises(LeapYearError):            
            is_leap_year("2024")  # String input
        with self.assertRaises(LeapYearError):
            is_leap_year(2024.5)  # Float input
        with self.assertRaises(LeapYearError):
            is_leap_year(None)  # None input
        with self.assertRaises(LeapYearError):
            is_leap_year([])  # List input
        with self.assertRaises(LeapYearError):
            is_leap_year('')  # empty string
            

    @patch("builtins.input", side_effect=["2024"]) # Simulate user entering 2024
    def test_get_year_valid_input(self, mock_input):
        """Test that get_year() correctly returns a valid year."""     
        self.assertEqual(get_year(), 2024) # Expect 2024 to be returned
        # Ensures it was called exactly once since I am testing one imput
        mock_input.assert_called_once()
    

    @patch("builtins.input", side_effect=["abcd", "-5", "2024"]) # Invalid inputs first
    def test_get_year_rejects_invalid_input(self, mock_input):
        """Test that get_year() rejects invalid input and keeps prompting."""
        self.assertEqual(get_year(), 2024)  # Should only return when a valid year is entered
    

    @patch("builtins.input", side_effect=["0"]) # Simulate user entering '0'
    @patch("leap.leap_year.exit_program")       # Mocking exit_program
    def test_get_year_calls_exit_program(self, mock_exit, mock_input):
        """Test that get_year() calls exit_program when 0 is entered."""
        try:
            get_year()
        except StopIteration:
            pass
        
        # Ensure exit_program() was called with "Goodbye!"
        mock_exit.assert_called_once_with("Goodbye!")


    @patch("sys.exit")  # Mock sys.exit() directly
    def test_exit_program_calls_sys_exit(self, mock_sys_exit):
        """Test that exit_program() calls sys.exit() with the correct message."""     
        exit_program("Goodbye!")  # Call the function

        # Assert that sys.exit() was called once with "Goodbye!"
        mock_sys_exit.assert_called_once_with("Goodbye!") 
    

if __name__ == "__main__":
    unittest.main()
