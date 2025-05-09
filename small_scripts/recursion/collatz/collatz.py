"""
    Recursive program that calculates how many steps it takes 
    to get to 1 if you start from n and recurse as indicated in README_COLLATZ.
    @datetime:: September 24, 2023 11:16 am (UTC-5)
    @author:: jac0der
"""


def main()->None:
    # get input from user
    str_number = input("Enter number: ")

    # call function to display result
    displaySteps(str_number)


def validateInput(number:str)->(bool, int):
    """
    Function to validate the user input to ensure a valid 
    numeric value is entered as well as a value >= 1.

    Args:
            str_number (str): value enetered by user.
    Returns:
            Tuple(bool, int): Tuple contaoining 2 elements. Index 0 is used 
                              to indicate by a boolean value if the user input
                              was valid; and index 1, is used to store the 
                              successfully cast integer value.
    """

    try:
        # try cast input to integer to ensure numeric value was entered
        number = int(number)

        # ensure positive whole numbers are entered >= 1
        if(number < 1):
            return (False, number)

        # input valid so return True
        return (True, number)
    
    except ValueError:
        # invalid input enetered
        return (False, number)


def collatz(number:str)->int:
    """
    Function to calculate the number of steps taken
    to get to 1, given a number n, using the algorithm
    for the collatz sequence, as outlined in the 
    README_COLLATZ read me file.
        
    Args:
            number (str): Value enetered by user.
    Returns:
            int: Number of steps taking to get to 1, from 
                 a number n.
    """

    step_count = 1;
    
    """
        list containing boolean indicating if validation
        was successful, and also the actual input entered
        by user.
    """ 
    validation = validateInput(number)

    if(validation[0]):

        # base case is met when number becomes 1, or is initially 1.
        if(validation[1] == 1):
            step_count = 0
        else:

            # check if number is even
            if(isEven(validation[1])):
                step_count += collatz(validation[1] / 2)
            else:
                step_count += collatz( (3 * validation[1]) + 1)
    else:
        # set step_count to -1 if user input validation failed.
        step_count = -1
        print(f"Invalid Input '{number}' entered...")

    return step_count


def isEven(number:int)->bool:
    """
    Function to determine if an integer is even or odd.
    Modulus operator wqas used to get the modulus of number / 2.  If there
    is no remainder, it means number is exactly
    divissible by 2, Thus number is even, otherwise odd.
    
    Args:
            number (int): Number entered by user.
    Returns:
            bool: rue if number is Even, otherwise False.
    """
    if( (number % 2) == 0 ):
        return True
    else:
        return False


def displaySteps(number:str)->None:
    """
        Function to display the results from collatz
        function execution.
    """

    steps = collatz(number)

    if( (steps == 0) and (number == '1') ):
        print(f"Already at '{number}', so 0 steps...")
    elif(steps > 0):
        print(f"Steps count is: {steps}")


if __name__ == '__main__':
    main()