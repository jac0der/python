''' 
    Program to convert from Celsius to Fahrenheit or, Fahrenheit to Celsius.

    @datetime:: February 8, 2025 2:42 am (UTC-5)
    @author:: jacoder
'''
import os 
import sys

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logging')))
import jaclog
logger = jaclog.configure('temperature_convertor', './tempconv.log')

CELCIUS_TO_FAHRENHEIT = 'CTF'
FAHRENHEIT_TO_CELCIUS = 'FTC'


def get_conversion_type():
    ''' 
    Get the type of conversion to perform.
    Returns:
            str: Conversion type code, CTF or FTC.
    '''
    logger.info('Getting conversion type.')
    while True:
        choice = input('\nChoose convertion type (0 to quit): ')

        if choice == '0':
            exit_program('Goodbye!')

        if choice == '1':
            logger.info(f'Conversion type is: {CELCIUS_TO_FAHRENHEIT}.')
            return CELCIUS_TO_FAHRENHEIT

        if choice == '2':
            return FAHRENHEIT_TO_CELCIUS
            logger.info(f'Conversion type is: {FAHRENHEIT_TO_CELCIUS}.')

        print(f'Invalid conversion option {choice} selected. Expecting 1 or 2.')
        logger.warning(f'Invalid conversion option {choice} selected. Expecting 1 or 2.')


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
    try:
        logger.info("Starting Temperature Converter.")
        print("Welcome to TEMPREATURE CONVERTER")
        print("Choose converstion type: ", end='\n')
        print("\t1 -> Celsious to Fahrenheit (CTF)",  end='\n')
        print("\t2 -> Fahrenheit to Celsious (FTC)",  end='\n')

        get_convertion_type()

    except Exception as ex:
        logger.exception("Error occured in main temperature conversion function.")


if __name__ == "__main__":
    main()