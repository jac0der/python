'''
    Determin if a number is either an even or an odd number.

    @datetime:: February 8, 2025 11:18 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
try:
    # When running as a module (for unittest)
    import even_odd.even_odd_constants as eoc
except ImportError:
    # When running the script directly
    import even_odd_constants as eoc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('even_odd', './even_odd.log')


def get_number():
    '''
    Get number to check if it is Even or Odd.

    Returns:
            int: User entered number to check for even or odd status.
    '''
    logger.info('Getting number from user.')
    while True:
        try:
            user_input = input("\nEnter number (q to quit): ").strip().lower()

            if user_input == 'q':
                exit_program(eoc.EXIT_MESSAGE)

            number = int(user_input)

            print(eoc.ENTERED_NUMBER.format(number))
            logger.info(eoc.ENTERED_NUMBER.format(number))

            return number

        except ValueError as ex:
            print(eoc.GET_NUMBER_WARNING)
            logger.warning(f'{eoc.GET_NUMBER_WARNING} \n {ex}')


def is_even(number):
    '''
    Check if specified number is an even or an odd number.

    Args:
            number (int): Number to check status of either even or odd.
    Returns:
            bool: True if number is even, otherwise, False.
    '''
    logger.info(f'Checking if {number} is even or odd.')

    if not isinstance(number, int):
        raise ValueError('Invalid Type: Expected an integer.')

    return number % 2 == 0


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
    """ Main function to start Even Odd Program. """
    
    try:
        logger.info("Starting The Even Odd Program...")

        while True:
            number = get_number()

            if is_even(number):
                print(eoc.RESULT_MESSAGE.format(number, eoc.EVEN))
                logger.info(eoc.RESULT_MESSAGE.format(number, eoc.EVEN))
            else:
                print(eoc.RESULT_MESSAGE.format(number, eoc.ODD))
                logger.info(eoc.RESULT_MESSAGE.format(number, eoc.ODD))
        
    except ValueError as ex:
        logger.error(f"ValueError: {ex}")

    except KeyboardInterrupt as ex:
        exit_program(f"\n{eoc.EXIT_MESSAGE}")

    except EOFError as ex:
        exit_program(f"\n{eoc.EXIT_MESSAGE}")

    except Exception as ex:
        logger.exception("Error occurred in main Even Odd function.")


if __name__ == "__main__":
    main()