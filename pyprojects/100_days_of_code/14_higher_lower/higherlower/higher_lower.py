'''
Guess a number between 1 and 100.

@datetime:: February 25, 2025 2:32 am (UTC-5)
@author:: jac0der
'''
from logging_custom import jaclog

logger = jaclog.configure('number_guess', './number_guess.log')

def main():
    """ Main function to start the Higher Lower Program. """
    try:
        logger.info("Starting the Higher Lower Game.")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{ngc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Higher Lower function.")


if __name__ == "__main__":
    main()