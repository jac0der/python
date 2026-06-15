"""
    Guess a number between a range of random numbers.

    @datetime:: June 15, 2026 8:19 am (UTC-5)
    @author:: jac0der
"""
import guess_constants as gn
from py_custom import jaclog,jacexit as je

logger = jaclog.configure('guess_number', './guess_number.log')


def main()->None:
    """ Main function to start Guess Number Program. """

    try:
        logger.info("Starting the Guess Number  Program...")
        while True:
            print("in main")
    
    except KeyboardInterrupt as ex:
        je.exit_program(f"\n{gn.EXIT_MESSAGE}", logger)

    except EOFError as ex:
        je.exit_program(f"\n{gn.EXIT_MESSAGE}", logger)

    except Exception as ex:
        logger.exception("Error occurred in main Guess Number function.")


if __name__ == "__main__":
    main()
