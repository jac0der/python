'''
    Check if a number is Prime.

    @datetime:: February 10, 2025 12:56 am (UTC-5)
    @author:: jac0der
'''
import sys
import os
import prime_checker_error as pce
import prime_checker_constants as pcc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('prime_checker', './prime_checker.log')


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
                exit_program(pcc.EXIT_MESSAGE)

            number = int(user_input)

            if number < 2:
                raise pce.PrimeCheckerError('Invalid input: Expecting a number >= 2.')

            print(pcc.ENTERED_NUMBER.format(number))
            logger.info(pcc.ENTERED_NUMBER.format(number))

            return number

        except ValueError as ex:
            print(pcc.GET_NUMBER_WARNING)
            logger.warning(f'{pcc.GET_NUMBER_WARNING} \n {ex}')

        except pce.PrimeCheckerError as ex:
            print(pcc.GET_PRIME_START_WARNING)
            logger.warning(f'{pcc.GET_PRIME_START_WARNING} \n {ex}')


def main():
    """ Main function to start the isPrime check Program. """
    try:
        while True:
            logger.info('Starting the Prime Checker Program.')
            get_number()

    except (KeyboardInterrupt, EOFError):
            print(f"\n{pcc.EXIT_MESSAGE}")
            return

    except Exception:
        logger.exception("Error occurred in main factorial function.")


if __name__ == "__main__":
    main()