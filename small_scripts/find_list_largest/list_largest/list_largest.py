'''
    Find the largest number within a list

    @datetime:: February 16, 2025 11:18 pm (UTC-5)
    @author:: jac0der
'''
from logging_custom import jaclog
import list_largest_constants as llc

logger = jaclog.configure('list_largest', './list_largest.log')


def main()->None:
    """ Main function to start the Largest List Item program.  """
    try:
        logger.info('Starting the largest list item program.')


    except (KeyboardInterrupt, EOFError):
        print(f"\n{llc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Find Largest List Item function.")


if __name__ == "__main__":
    main()






