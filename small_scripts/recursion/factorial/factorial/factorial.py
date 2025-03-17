"""
    Python factorial implementation for positive 
    whole numbers.

    @datetime:: September 23, 2023 1:19 am (UTC-5)
    @author:: jac0der
"""
import sys
import os
import math
import factorial_error as fe
import factorial_constants as fc
from logging_custom import jaclog

logger = jaclog.configure('factorial', './factorial.log')


def get_number()->int:
    '''
    Get number for factorial calculation.

    Returns:
            int: User entered number for factorial calculation.
    '''
    logger.info('Getting number for factorial calculation.')

    while True:
        try:
            user_input = input("\nEnter number (q to quit): ").strip().lower()

            if user_input == 'q':
                exit_program(fc.EXIT_MESSAGE)

            number = int(user_input)

            if number < 0:
                raise fe.FactorialError('Invalid Input: Expecting only positive integers.')

            print(fc.ENTERED_NUMBER.format(number))
            logger.info(fc.ENTERED_NUMBER.format(number))

            return number

        except ValueError as ex:
            print(fc.GET_NUMBER_WARNING)
            logger.warning(f'{fc.GET_NUMBER_WARNING} \n {ex}')

        except fe.FactorialError as ex:
            print(fc.GET_NUMBER_WARNING)
            logger.warning(f'{fc.GET_NUMBER_WARNING} \n {ex}')


def factorial(number:int)->int:
    '''
        Find the factorial of a number.

        Args:
                number (int): Number to calculate factorial.
        Returns:   
                int: Factorial of input number.
    '''
    if not isinstance(number, int):
        raise TypeError('Invalid Type: Expected an integer.')

    if number < 0:
        raise fe.FactorialError('Invalid Input: Expecting only positive integers.')

    if number in [0, 1]:
        return 1

    return number * factorial(number - 1)
    #return math.factorial(number)


def factorial_iterative(number:int)->int:
    if not isinstance(number, int):
        raise TypeError('Invalid Type: Expected an integer.')
    
    if number < 0:
        raise fe.FactorialError('Invalid Input: Expecting only positive integers.')

    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def exit_program(message:str, code:int=0)->None:
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    print(message)
    sys.exit(code)


def main()->None:
    """ Main function to start the factorial program.  """
    try:
        logger.info('Starting the factorial program.')

        while True:
            fact = factorial(get_number())

            print(f"Factorial is: {fact}")
            logger.info(f"Factorial is: {fact}")

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except fe.FactorialError as ex:
        logger.error(f"FactorialError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{fc.EXIT_MESSAGE}")
        return

    except Exception as ex:
        logger.exception("Error occurred in main factorial function.")


if __name__ == "__main__":
    main()
