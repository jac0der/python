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



def main():
    '''
    Main function to trigger the leap year program.
    '''
    try:
        if is_leap_year(2001):
            print(f'Year {2001} was a leap year.')
        else:
            print(f'Year {2001} was NOT a leap year.')

    except leap_error.LeapYearError as ex:
        logger.error(f'Leap Year error: {ex}')
        sys.exit(f'Error: {ex}. Please check the logs for details')

    except Exception:
        logger.exception('Error occured in main() leap year function.')
        sys.exit('An error occured. Please check the logs for details.')


if __name__ == "__main__":
    main()