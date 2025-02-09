'''
    Determin if a number is either an even or an odd number.

    @datetime:: February 8, 2025 11:18 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
import even_odd_constants as eoc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logging')))
import jaclog
logger = jaclog.configure('even_odd', './even_odd.log')


def exit_program(message, code=0):
    '''
    Centralized exit function to handle program termination.

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
        
    except KeyboardInterrupt as ex:
        exit_program(f"\n{eoc.EXIT_MESSAGE}")

    except EOFError as ex:
        exit_program(f"\n{eoc.EXIT_MESSAGE}")

    except Exception as ex:
        logger.exception("Error occurred in main Even Odd function.")


if __name__ == "__main__":
    main()