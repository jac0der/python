'''
    Create a calculator app to perform basic mathematical operations.

    @datetime:: January 29, 2025 6:37 am (UTC-5)
    @author:: jacoder
'''
import os, sys, operator, art

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('calculator_100days', './calculator.log')


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
            return float(input(prompt))
        except ValueError:
            logger.error('Invalid number entered for math calculation.' + '\n' + 'Please enter a valid numeric value.')


def get_operation():
    ''' 
        Function used to list the available operations for the calculator.
        
        Args:
            none

        Returns: 
            str:  selected math operation.
    '''
    logger.info('Getting math operation.') 

    print("\nAvailable Math operations:")
    for op in OPERATIONS:
        print(op)

    while True:
        operation = input("Pick an operation: ").strip()
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
    try:
        logger.info(f'Calculating {first_number} {operation} {second_number}') 
        return OPERATIONS[operation](first_number, second_number)
    except ZeroDivisionError as ex:
        logger.error(f'Error: Cannot divide {first_number} by {second_number}.')
        logger.error(f'Error details: {ex}')        
        return None
    except Exception as ex:
        logger.error(f'An unexpected error occurred while calculating {first_number} {operation} {second_number}.')
        logger.error(f'Error details: {ex}')  
        logger.error('Please verify your inputs and try again.')
        return None


def main():
    ''' main function to run the calculator'''
    logger.info('Starting calculator.')
    print(art.logo)
    print("Welcome to the Calculator App!")

    try:
        while True:
            logger.info('Getting first number.')           
            first_number = get_number("What's the first number?: ")
            continue_calculating = True         

            while continue_calculating:
                
                operation = get_operation()

                logger.info('Getting second number.') 
                second_number = get_number("What's the next number?: ")
                    
                result = calculate(first_number, second_number, operation)

                if result is not None:
                    logger.info(f'Result is: {result}.')
                    print(f"{first_number} {operation} {second_number} = {round(result, 2)}")

                    # Continue or restart
                    choice = input("Type 'y' to continue with this result, or 'n' to start a new calculation: ").lower()
                    if choice == 'y':
                        # reset first number as current evaluation to be used to continue
                        # calculating with next second number inputted.
                        first_number = result
                    else:
                        os.system('cls||clear')  # Clear screen
                        continue_calculating = False
                else:
                    logger.warning(f'No result from calculation of {first_number} {operation} {second_number}.')
                    continue  # Skip result display if calculation failed
           
    except Exception as ex:
        logger.error("Error occured in main calculator function." + '\n' + str(ex))


if __name__ == "__main__":
    main()