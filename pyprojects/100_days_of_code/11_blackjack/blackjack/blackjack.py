'''
    Create a black jack game.

    @datetime:: February 12, 2025 8:03 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
import blackjack_constants as bjc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../logging')))
import jaclog
logger = jaclog.configure('blackjack', './blackjack.log')


def main():
    """ Main function to start the blackjack program. """
    try:
        logger.info('Starting the blackjack game.')
        
    except (KeyboardInterrupt, EOFError):
        print(f"\n{bjc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main BlackJack function.")

if __name__ == "__main__":
    main()