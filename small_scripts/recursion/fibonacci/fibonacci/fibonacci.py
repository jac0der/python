'''
    Print the first n numbers of the Fibonacci sequence.

    @datetime:: February 9, 2025 8:28 am (UTC-5)
    @author:: jac0der
'''
import sys
import os
import fibonacci_constants as fc
import fibonacci_error as fe

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../logging')))
import jaclog
logger = jaclog.configure('fibonacci', './fibonacci.log')


def get_position():
    '''
    Get the position in the Fibinacci sequence to get value for.
    
    Returns:
            int: Fibonacci value for posirion.
    '''
    logger.info('Getting fibonacii position from user.')
    while True:
        try:
            user_input = input('\nEnter Fibonacii position (q to quit): ').strip().lower()
            if user_input == 'q':
                exit_program(fc.EXIT_MESSAGE)

            position = int(user_input)

            print(fc.ENTERED_POSITION.format(position))
            logger.info(fc.ENTERED_POSITION.format(position))

            return position

        except ValueError as ex:
            print(fc.GET_NUMBER_WARNING)
            logger.warning(f'{fc.GET_NUMBER_WARNING} \n {ex}')


def fibonacci(position):
    ''' 
    Find the Fibonacci number for the Fibonacci position entered.

    Args:
            position (int): The nth position of the Fibonaccii sequence
            to get the actual value.
    Returns:
            int: Fibonacci value for position entered.
    '''
    if not isinstance(position, int):
        raise ValueError('Invalid Type: Expected an integer.')

    if position < 0:
        raise fe.FibonacciError('Invalid Input: Expected positive whole numbers.')

    if position == 0:
        return 0
    
    if position == 1:
        return 1

    return fibonacci(position - 1) + fibonacci(position - 2)


def display_nth_sequence(position):
    '''
    Print the nth numbers of the Fibonacii sequence.

    Args:
            position (int): The number of numbers of the 
            Fibonacii sequence to print.
    '''
    if not isinstance(position, int):
        raise ValueError('Invalid Type: Expected an integer.')

    if position < 0:
        raise fe.FibonacciError('Invalid Input: Expected positive whole numbers.')

    logger.info(f"Displaying the first {position} Fibonacii numbers.")
    for n in range(position):
        print(fibonacci(n))
    

def exit_program(message, code=0):
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)


def main():
    """ Main function to start the Fibonacci Program. """
    try:
        while True:
                logger.info("Starting Fibonacci Program...")
                display_nth_sequence(get_position())
        
    except ValueError as ex:
        logger.error(f"ValueError: {ex}")

    except fe.FibonacciError as ex:
        logger.error(f"FibonacciError: {ex}")

    except KeyboardInterrupt as ex:
        exit_program(f"\n{fc.EXIT_MESSAGE}")

    except EOFError as ex:
        exit_program(f"\n{fc.EXIT_MESSAGE}")

    except Exception as ex:
        pass
        logger.exception("Error occurred in main Fibonacci function.")


if __name__ == "__main__":
    main()