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
    Get a number from the user to check for primality.

    Returns:
            int: User-entered number to check for primality.
    '''
    logger.info('Getting number from user.')
    while True:
        try:
            user_input = input("\nEnter number (q to quit): ").strip().lower()

            if user_input == 'q':
                exit_program(pcc.EXIT_MESSAGE)

            number = int(user_input)

            if number < 0:
                raise pce.PrimeCheckerError(pcc.PRIME_NUMBER_INVALID)

            print(pcc.ENTERED_NUMBER.format(number))
            logger.info(pcc.ENTERED_NUMBER.format(number))

            return number

        except ValueError as ex:
            print(pcc.GET_NUMBER_WARNING)
            logger.warning(f'{pcc.GET_NUMBER_WARNING} \n {ex}')

        except pce.PrimeCheckerError as ex:
            print(pcc.GET_PRIME_START_WARNING)
            logger.warning(f'{pcc.GET_PRIME_START_WARNING} \n {ex}')


def is_prime(number):
    '''
    Check if number is a prime number.

    Args:
            number (int): The number to check for primality.
    Returns:
            bool: True if number is prime, otherwise, False.
    '''
    logger.info(f"Checking primality of {number}.")

    if not isinstance(number, int):
        raise ValueError('Invalid Type: Expected an integer.')
    
    if number < 0:
        raise pce.PrimeCheckerError(pcc.PRIME_NUMBER_INVALID)

    if number < 2:
        return False

    if number in (2,3):
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    # Every prime number greater than 2 and 3 can be represented as 6n+1 or 6n-1.
    # solve for n
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6  # Check numbers in 6k ± 1 form

    return True
  

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
    """ Main function to start the isPrime check Program. """
    try:
        logger.info('Starting the Prime Checker Program.')
        while True:            
            number = get_number()
            
            if is_prime(number):
                print(f"Result: {number} is Prime")
                logger.info(f"Result: {number} is Prime")
            else:
                print(f"Result: {number} is NOT Prime")
                logger.info(f"Result: {number} is NOT Prime")

    except ValueError as ex:
        logger.error(f"ValueError: {ex}")
    
    except pce.PrimeCheckerError as ex:
        logger.error(f"PrimeCheckerError: {ex}")

    except (KeyboardInterrupt, EOFError):
            print(f"\n{pcc.EXIT_MESSAGE}")
            return

    except Exception:
        logger.exception("Error occurred in main Prime Checking function.")


if __name__ == "__main__":
    main()