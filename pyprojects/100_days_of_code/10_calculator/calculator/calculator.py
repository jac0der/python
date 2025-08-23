'''
    Create a calculator app to perform basic mathematical operations.

    @datetime:: January 29, 2025 6:37 am (UTC-5)
    @author:: jacoder
'''
import os 
import sys
import operator
from logging_custom import jaclog

try:
    # When running as a module (for unittest)
    from calculator.art import logo  
except ImportError:
    # When running the script directly
    from art import logo 

logger = jaclog.configure('calculator_100days', './calculator.log')

EXIT_MESSAGE = 'Goodbye!'
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def get_number(prompt):
    '''
        Handles numeric input with validation.

        Args:
                prompt (str): text to instruct user on which number to enter.
        Returns:
                float: the converted number from the entered user number.
    '''
    while True:
        try:
            number = float(input(prompt))

            if number == 0:
                exit_program("Goodbye!")

            return number
        except ValueError:
            logger.warning('Invalid number entered for math calculation.' + '\n' + 'Please enter a valid numeric value.')


def get_operation():
    ''' 
        Function used to list the available operations for the calculator.
        Returns: 
            str:  selected math operation.
    '''
    logger.info('Getting math operation.') 
    
    print("\nAvailable Math operations:")
    for op in OPERATIONS:
        print(op)

    while True:
        operation = input("Pick an operation (0 to quit): ").strip()
        
        if operation == '0':
            exit_program('Goodbye!')            

        if operation in OPERATIONS:
            logger.info(f'Selected operation is {operation}.')
            return operation

        logger.warning('Invalid operation. Please choose from the list of math operations.')


def calculate(first_number, second_number, operation):
    '''
    Performs the calculation based on the selected operation.

    Args:
            first_number (float): First number of the equation.
            second_number (float): Second number of the equation.
            operation (str): The math operation to  perform.
    Returns: 
            float: The result of the math operation selected.
    '''
    if not isinstance(first_number, float):
        raise ValueError(f'Invalid type for first number. Expected a float.')

    if not isinstance(second_number, float):
        raise ValueError(f'Invalid type for second number. Expected a float.')

    if operation.strip() == '/' and second_number == 0:
        raise ZeroDivisionError
        
    logger.info(f'Calculating {first_number} {operation} {second_number}')
    return round(OPERATIONS[operation](first_number, second_number), 2)
 

def exit_program(message, code=0):
    '''
    Centralized exit function to handle program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)


def main():
    ''' main function to run the calculator'''
    logger.info('Starting calculator.')
    print(logo)
    print("Welcome to the Calculator App!")

    try:
        while True:
            logger.info('Getting first number.')           
            first_number = get_number("What's the first number? (0 to quit): ")
            logger.info(f'first_number is {first_number}.')

            continue_calculating = True         

            while continue_calculating:                
                operation = get_operation()

                logger.info('Getting second number.') 
                second_number = get_number("What's the next number? (0 to quit): ")
                logger.info(f'second_number is {second_number}.')

                try:
                    result = calculate(first_number, second_number, operation)

                except ValueError:
                    logger.warning('Invalid inputs to calculate function.')
                    continue
                except ZeroDivisionError as ex:
                    print('Cannot divide {first_number} by {second_number}.')
                    logger.warning(f'Cannot divide {first_number} by {second_number}.')
                    continue

                logger.info(f'Result is: {result}.')                  
                print(f"{first_number} {operation} {second_number} = {result}")

                # Continue or restart
                choice = input("Type 'y' to continue with this result, or 'n' to start a new calculation (0 to quit): ").lower()
                
                if choice == '0':
                    exit_program('Goodbye!')

                if choice == 'y':
                    # reset first number as current evaluation to be used to continue
                    # calculating with next second number inputted.
                    first_number = result
                else:
                    os.system('cls||clear')  # Clear screen
                    continue_calculating = False

    except (KeyboardInterrupt, EOFError):
        exit_program(f"\n{EXIT_MESSAGE}")

    except Exception as ex:
        logger.exception("Error occured in main calculator function.")
        exit_program('An error occured. Please check the logs for details.')


if __name__ == "__main__":
    main()