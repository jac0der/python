'''
Guess a number between 1 and 100.

@datetime:: February 25, 2025 2:32 am (UTC-5)
@author:: jac0der
'''

import sys
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
    if not isinstance(minimum, int) or not isinstance(maximum, int):
        raise TypeError(f"Invalid Input: Expected Type int for both minimum {minimum} and maximum {maximum} imputs.")

    logger.info(f"Getting the random number between {minimum} and {maximum}.")
    return random.randint(minimum, maximum)


def get_user_choice(random_number:int)->int:
    """
    Gets user choice of difficulty level to try and guess number.

    Args:
            random_number (int): The generated random number to try and guess.
    Returns:
            int: Return 1 if random number was guessed successfully, otherwise, 0.    
    """
    if not isinstance(random_number, int):
        raise TypeError(f"Invalid Input: Expected Type int for random_number ({random_number}) imput.")

    logger.info("Getting the user's choice.")

    while True:

        print(f"\nI'm thinking of a number between {ngc.MINIMUM_GUESS} and {ngc.MAXIMUM_GUESS}.")
        choice = input("Choose a difficulty. Type 'easy' or 'hard' (q to quit): ").strip().lower()

        if choice == 'q':
            exit_program(ngc.EXIT_MESSAGE)
        elif choice == 'easy':
            return guess(random_number, ngc.LEVEL_EASY)
        elif choice == 'hard':
            return guess(random_number, ngc.LEVEL_HARD)
        else:
            print("\nInvalid input, please enter 'easy' or 'hard'.")


def guess(guess_number:int, attempts:int)->int:
    """
    Gets user guess and compare with the random number.

    Args:
            guess_number (int): The generated random number to try and guess.
            attempts (int): The number of guess tries based on selected difficulty level.
    Returns:
            int: Return 1 if random number was guessed successfully, otherwise, 0.    
    """
    if not isinstance(guess_number, int) or not isinstance(attempts, int):
        raise TypeError(f"Invalid Input: Expected Type int for both guess_number {guess_number} and attempts {attempts} imputs.")

    logger.info('Starting the number guessing.')

    counter = attempts
    for _ in range(attempts):
        try:
            logger.info(f"{counter} attempts remaning.")
            print(f"You have {counter} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            logger.info(f"Current guess is: {guess}.")

            if guess == guess_number:
                return 1
            elif guess < guess_number:
                if counter > 1:
                    print(ngc.GUESS_MESSAGE.format('low'))
                    logger.info(ngc.GUESS_MESSAGE.format('low'))
            else:
                if counter > 1:
                    print(ngc.GUESS_MESSAGE.format('high'))
                    logger.info(ngc.GUESS_MESSAGE.format('high'))

        except ValueError as ex:
            print(ngc.GET_GUESS_WARNING)
            logger.warning(f"{ngc.GET_GUESS_WARNING} \n {ex}")

        counter -= 1

    # failed to guess random number.
    return 0


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
    """ Main function to start the Number Guessing program. """
    try:
        logger.info('Starting the Number Guessing program.')
        print(art.logo)
        print('Welcome to the Number Guessing Game!')

        number = get_random_number(ngc.MINIMUM_GUESS, ngc.MAXIMUM_GUESS)
        logger.info(f"Generated random number is: {number}.")

        if get_user_choice(number) == 1:
            print(ngc.SUCCESS_MESSAGE.format(number))
            logger.info(ngc.SUCCESS_MESSAGE.format(number))
        else:
            print(ngc.FAILED_MESSAGE)
            logger.info(ngc.FAILED_MESSAGE)

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except ValueError as ex:
        logger.error(f"ValueError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{ngc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Number Guessing function.")


if __name__ == "__main__":
    main()