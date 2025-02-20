'''
    Remove duplicates from a list.

    @datetime:: February 19, 2025 11:29 pm (UTC-5)
    @author:: jac0der
'''
from logging_custom import jaclog
import remove_dups_constants as rdc

logger = jaclog.configure('list_remove_dups', './list_remove_dups.log')


def main():
    """ Main function to start the Remove Duplicates program """
    try:
        logger.info('Starting the remove dupliates program.')
    
    except (KeyboardInterrupt, EOFError):
        print(f"\n{rdc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Find Largest List Item function.")


if __name__ == "__main__":
    main()