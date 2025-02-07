'''
    Create a program to determine if a year is a leap year.

    @datetime:: February 05, 2025 8:43 am (UTC-5)
    @author:: jac0der
'''
import os 
import sys
try:
    # When running as a module (for unittest)
    from leap.leap_error import LeapYearError  
except ImportError:
    # When running the script directly
    from leap_error import LeapYearError 

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../logging')))
import jaclog
logger = jaclog.configure('leapyear_100days', './leapyear.log')


def is_leap_year(year):
    ''' 
    Determine if year is a leap year.

    Args:
             year (int): Year to determine whether it is a leap year or not.
    Returns: 
             bool: True if year is a leap year, otherwise, False.
    '''
    logger.info(f'Determining leap year status for year {year}.')
    if not isinstance(year, int):
        raise LeapYearError(f'Invalid year type: {year}. Expected an integer.')

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_year():
    '''
    Retrieve the year from user to check if it is a leap year.

    Returns:
            int: The year to check for leap year status.
    '''    
    while True:
        try:
            year = int(input('\nEnter year(0 to quit): '))

            if year == 0:
                exit_program('Goodbye!')

            if year < 1000 or year > 9999:
                logger.warning('Invalid year entered.' + '\n' + 'Year must be a four-digit number.')
                continue

            logger.info(f'Entered year is: {year}.')
            return year
        except ValueError:
            logger.warning('Invalid year entered.' + '\n' + 'Please enter a valid numeric value.')


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
    '''
    Main function to trigger the leap year program.
    '''
    try:
        while True:           
            year = get_year()

            if is_leap_year(year):
                print(f'Year {year} is a leap year.')
                logger.info(f'Year {year} is a leap year.')
            else:
                print(f'Year {year} is NOT a leap year.')
                logger.info(f'Year {year} is NOT a leap year.')

    except LeapYearError as ex:
        logger.error(f'Leap Year error: {ex}')
        exit_program(f'Error: {ex}. Please check the logs for details')

    except Exception:
        logger.exception('Error occured in main() leap year function.')
        exit_program('An error occured. Please check the logs for details.')


if __name__ == "__main__":
    main()