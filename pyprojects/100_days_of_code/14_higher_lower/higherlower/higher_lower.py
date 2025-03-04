'''
Create the higher lower game, guess from among two options
which has the higher value.

@datetime:: March 2, 2025 11:49 pm (UTC-5)
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