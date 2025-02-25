'''
Guess a number between 1 and 100.

@datetime:: February 25, 2025 2:32 am (UTC-5)
@author:: jac0der
'''

import art
import random
from logging_custom import jaclog
import number_guess_constants as ngc

logger = jaclog.configure('number_guess', './number_guess.log')


def get_random_number(minimum:int, maximum:int)->int:
    """
    Generate a random number between a specified minimum and maximum values.

    Args:
            minimum (int): The lower bound value from which random number is selected.
            maximum (int): The upper bound value from which random number is selected.
    Returns:
            int: The generated random number from the specified range.
    """
    if not isinstance(minimum, int) and not isinstance(maximum, int):
        raise TypeError(f"Invalid Input: Expected Type int for both minimum {minimum} and maximum {maximum} imputs.")

    logger.info(f"Getting the random number between {minimum} and {maximum}.")
    return random.randint(minimum, maximum)


def main()->None:
    """ Main function to start the Number Guessing program. """
    try:
        logger.info('Starting the Number Guessing program.')
        print(art.logo)

        number = get_random_number(ngc.MINIMUM_GUESS, ngc.MAXIMUM_GUESS)

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{ngc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Number Guessing function.")


if __name__ == "__main__":
    main()