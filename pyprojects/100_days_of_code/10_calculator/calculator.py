'''
    Create a calculator app to perform basic mathematical operations.

    @datetime:: January 29, 2025 6:37 am (UTC-5)
    @author:: jacoder
'''
import os, operator, art


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
            print("Invalid number. Please enter a valid numeric value.")


def get_operation():
    ''' 
        Function used to list the available operations for the calculator.
        
        Args:
            none

        Returns: 
            str:  selected math operation.
    '''
    print("\nAvailable operations:")
    for op in OPERATIONS:
        print(op)

    while True:
        operation = input("Pick an operation: ").strip()
        if operation in OPERATIONS:
            return operation
        print("Invalid operation. Please choose from the list.")


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
        return OPERATIONS[operation](first_number, second_number)
    except ZeroDivisionError as ex:
        print(f"Error: Cannot divide {first_number} by {second_number}.")
        print(f"Error details: {ex}")
        return None
    except Exception as ex:
        print(f"An unexpected error occurred while performing '{first_number} {operation} {second_number}'.")
        print(f"Error details: {ex}")
        print("Please verify your inputs and try again.")
        return None


def main():
    ''' main function to run the calculator'''
    print(art.logo)
    print("Welcome to the Calculator App!")

    try:
        while True:           
            first_number = get_number("What's the first number?: ")
            continue_calculating = True         

            while continue_calculating:

                operation = get_operation()
                second_number = get_number("What's the next number?: ")
                    
                result = calculate(first_number, second_number, operation)

                if result is not None:
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
                    continue  # Skip result display if calculation failed
           
    except Exception as ex:
        print("Error occured." + '\n' + str(ex))


if __name__ == "__main__":
    main()