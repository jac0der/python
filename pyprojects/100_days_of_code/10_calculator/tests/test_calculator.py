import unittest
from unittest.mock import patch
from calculator.calculator import calculate, get_number, get_operation, exit_program

class TestCalculator(unittest.TestCase):

    def test_calculate_invalid_first_number_inputs(self):
        ''' Test invalid inputs for first number. '''
        # invalid first number   
        with self.assertRaises(ValueError):                     
            calculate(6, 2.0, '/')          # integer
        with self.assertRaises(ValueError):  
            calculate('6', 2.0, '/')        # string

            # other invalid inputs
        with self.assertRaises(ValueError):  
            calculate(None, 2.0, '/')
        with self.assertRaises(ValueError):  
            calculate(True, 2.0, '/')
        with self.assertRaises(ValueError):  
            calculate(dict(), 2.0, '/')


    def test_calculate_invalid_second_number_inputs(self):
        ''' Test invalid inputs for second number. '''
        with self.assertRaises(ValueError):  
            calculate(6.0, 2, '/')          # integer
        with self.assertRaises(ValueError):  
            calculate(6, '2.0', '/')        # string

            # other invalid inputs
        with self.assertRaises(ValueError):  
            calculate(8.9, None, '/')
        with self.assertRaises(ValueError):  
            calculate(4.358, False, '/')
        with self.assertRaises(ValueError):  
            calculate(75.45, [], '/')

    
    def test_calculate_division_by_zero(self):
        ''' Test division by zero raising ZeroDivisionError. '''
        with self.assertRaises(ZeroDivisionError):  
            calculate(8.9, 0.0, '/')


    def test_calculate_valid_inputs(self):  
        ''' Test valid inputs to the calculate function.'''       
        self.assertEqual(calculate(6.0, 2.0, '/'), 3.0)
        self.assertEqual(calculate(3.0, 2.4, '/'), 1.25)
        self.assertEqual(calculate(-9.0, 2.0, '/'), -4.5)
        
        self.assertEqual(calculate(100.3375, 2.733, '*'), 274.22)
        self.assertEqual(calculate(94.95, 67.89, '*'), 6446.16)
        self.assertEqual(calculate(0.0, 5.5, '*'), 0)  # Multiplication with zero
        self.assertEqual(calculate(-3.0, 4.0, '*'), -12)

        self.assertEqual(calculate(-7.0, 2.0, '+'), -5.0)
        self.assertEqual(calculate(-8.0, -2.4, '+'), -10.4)
        self.assertEqual(calculate(-8.0, -0.0, '+'), -8)
        self.assertEqual(calculate(15.0, -5.0, '+'), 10)
        self.assertAlmostEqual(calculate(1e10, 1e-10, '+'), 1e10, places=5)  # Large + small

        self.assertEqual(calculate(7.3, 8.9, '-'), -1.6)
        self.assertEqual(calculate(33.33, 4.0, '-'), 29.33)
        self.assertEqual(calculate(0.0, -4.0, '-'), 4.0)

    
    @patch("builtins.input", side_effect=["7"])
    def test_get_number_valid_input(self, mock_input):
        ''' Test a valid input to get number and ensure input is called only once. '''
        self.assertEqual(get_number(''), 7.0)
        mock_input.assert_called_once()


    @patch("builtins.input", side_effect=["#", "@", "$", "5.1"])
    def test_get_number_rejects_invalid_inputs(self, mock_input):
        ''' Test get_number rejects initial invalid inputs before a valid input '''
        self.assertEqual(get_number(''), 5.1)

    
    @patch("builtins.input", side_effect=["0"])
    @patch("calculator.calculator.exit_program")
    def test_get_number_calls_exit_program(self, mock_exit ,mock_input):
        ''' Test get_number exits program with Goodbye! when 0 is entered. '''
        get_number('')
        mock_exit.assert_called_once_with("Goodbye!")


    @patch("builtins.input", side_effect=["abc", "3.5"])
    @patch("calculator.calculator.logger.warning")  # Mock logger
    def test_get_number_logs_warning_on_invalid_input(self, mock_logger, mock_input):
        ''' Test get_number logs a warning message when invalid input is entered. '''
        self.assertEqual(get_number(''), 3.5)
        mock_logger.assert_called_with('Invalid number entered for math calculation.\nPlease enter a valid numeric value.')

    
    @patch("sys.exit")
    def test_exit_program_calls_sys_exit(self, mock_sys_exit):
        ''' Test that exit_program() calls sys.exit() with the correct message. '''    
        exit_program("Goodbye!")

        # Assert that sys.exit() was called once with "Goodbye!"
        mock_sys_exit.assert_called_once_with("Goodbye!") 

    
    @patch("builtins.input", side_effect=["0"])
    @patch("calculator.calculator.exit_program")
    def test_get_operation_calls_exit_program(self, mock_exit, mock_input):
        ''' Test get_operation exits program with Goodbye! when 0 is entered. '''
        try:
            get_operation()
        except StopIteration:
            pass
        
        mock_exit.assert_called_once_with("Goodbye!") 

    
    @patch("builtins.input", side_effect=["+", "-", "*", "/"])
    def test_get_operation_returns_valid_operation(self, mock_input):
        ''' Test get_operation returns each valid operation once entered. '''

        for expected_op in ["+", "-", "*", "/"]:
            self.assertEqual(get_operation(), expected_op)


    @patch("builtins.input", side_effect=["f", "^","@", "d"])
    def test_get_operation_continue_prompt_on_invalid_operation(self, mock_input):
        ''' 
        Test get_operation continues to prompt for operation if no valid 
        operation is entered. Raises a StopIteration Exception.
        '''
        with self.assertRaises(StopIteration):
            get_operation()


    @patch("builtins.input", side_effect=["f", "^","@", "d", "/"])
    def test_get_operation_continue_prompt_until_valid_operation(self, mock_input):
        ''' 
        Test get_operation continues to prompt for operation until a valid 
        operation is entered.
        '''
        self.assertEqual(get_operation(), "/")


    @patch("builtins.input", side_effect=["#", "/"])
    @patch("calculator.calculator.logger.warning")  # Mock logger
    def test_get_operation_logs_warning_if_operation_not_in_list(self, mock_logger, mock_input):
        ''' Test get_operation logs a warning message when invalid input is entered. '''
        self.assertEqual(get_operation(), "/")
        mock_logger.assert_called_with('Invalid operation. Please choose from the list of math operations.')


if __name__ == '__main__':
    unittest.main()