'''
    Create a program to determine if a year is a leap year.

    @datetime:: February 05, 2025 8:43 am (UTC-5)
    @author:: jac0der
'''
import os, sys, leap_error

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
             bool: True if year is a leap year, otherwise, False, year is not a leap year.
    '''
    try:
        logger.info(f'Determining leap year status for year {year}.')
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False            
    except Exception as ex:
        logger.exception(f'An error occured determining if {year} is a leap year.')
        raise leap_error.LeapYearError(f'An error occured during the leap year determination process for year {year}.') from ex



def get_year():
    '''
    Retrieve the year from user to check if it is a leap year.

    Returns:
            int: The year to check for leap year status.
    '''
    try:
        while True:
            try:
                year = int(input('\nEnter year(0 to quit): '))

                if year == 0:
                    logger.info('Bye...User exited program.')
                    sys.exit('Bye...')

                if len(str(year)) != 4:
                    logger.warning('Invalid year entered.' + '\n' + 'Year must be 4 digits.')
                    continue

                logger.info(f'Entered year is: {year}.')
                return year
            except ValueError:
                logger.warning('Invalid year entered.' + '\n' + 'Please enter a valid numeric value.')
                continue

    except Exception:
        logger.exception('Error occurred while getting year from user.')
        return None


def main():
    '''
    Main function to trigger the leap year program.
    '''
    try:
        while True:
            year = get_year()

            if year is not None:

                if is_leap_year(year):
                    print(f'Year {year} is a leap year.')
                    logger.info(f'Year {year} is a leap year.')
                else:
                    print(f'Year {year} is NOT a leap year.')
                    logger.info(f'Year {year} is NOT a leap year.')
            else:
                logger.warning('No year retrieved from user.')
                sys.exit('No year retrieved from user. Please check the logs for more details.')


    except leap_error.LeapYearError as ex:
        logger.error(f'Leap Year error: {ex}')
        sys.exit(f'Error: {ex}. Please check the logs for details')

    except Exception:
        logger.exception('Error occured in main() leap year function.')
        sys.exit('An error occured. Please check the logs for details.')


if __name__ == "__main__":
    main()