'''
    Check if a number is Prime.

    @datetime:: February 10, 2025 12:56 am (UTC-5)
    @author:: jac0der
'''
import sys
import os

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('prime_checker', './prime_checker.log')


def main():
    """ Main function to start the isPrime check Program. """
    try:
        logger.info('Starting the Prime Checker Program.')

    except Exception:
        pass


if __name__ == "__main__":
    main()