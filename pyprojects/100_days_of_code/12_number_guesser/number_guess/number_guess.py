'''
Guess a number between 1 and 100.

@datetime:: February 25, 2025 2:32 am (UTC-5)
@author:: jac0der
'''

import art
from logging_custom import jaclog
import number_guess_constants as ngc

logger = jaclog.configure('number_guess', './number_guess.log')


def main()->None:
    """ Main function to start the Number Guessing program. """
    try:
        logger.info('Starting the Number Guessing program.')
        print(art.logo)

    except (KeyboardInterrupt, EOFError):
        print(f"\n{ngc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Number Guessing function.")


if __name__ == "__main__":
    main()