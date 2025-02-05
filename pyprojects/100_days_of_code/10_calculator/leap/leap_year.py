'''
    Create a program to determine if a year is a leap year.

    @datetime:: February 05, 2025 8:43 am (UTC-5)
    @author:: jac0der
'''
import os, sys

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
    except Exception:
        logger.exception(f'An error occured determining if {year} is a leap year.')



def main():
    if is_leap_year(2000):
        print(f'Year {2000} was a leap year.')


if __name__ == "__main__":
    main()