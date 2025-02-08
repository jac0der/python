''' 
    Program to convert from Celsius to Fahrenheit or, Fahrenheit to Celsius.

    @datetime:: February 8, 2025 2:42 am (UTC-5)
    @author:: jacoder
'''
import os 
import sys
import tempconv_error

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logging')))
import jaclog
logger = jaclog.configure('temperature_convertor', './tempconv.log')

# connstants definitions
EXIT_MESSAGE = 'Goodbye!'
INVALID_INPUT = 'Invalid Input'
CELCIUS_TO_FAHRENHEIT = 'CTF'
FAHRENHEIT_TO_CELCIUS = 'FTC'


def get_conversion_type():
    ''' 
    Get the type of conversion to perform.
    Returns:
            str: Conversion type code, CTF or FTC.
    '''
    logger.info('Getting conversion type.')
    print("\nChoose conversion type: ", end='\n')
    print("\t1 -> Celsius to Fahrenheit (CTF)",  end='\n')
    print("\t2 -> Fahrenheit to Celsius (FTC)",  end='\n')

    while True:
        choice = input('\nChoose convertion type (0 to quit): ')

        if choice == '0':
            exit_program(EXIT_MESSAGE)

        if choice == '1':
            logger.info(f'Conversion type is: {CELCIUS_TO_FAHRENHEIT}.')
            return CELCIUS_TO_FAHRENHEIT

        if choice == '2':
            logger.info(f'Conversion type is: {FAHRENHEIT_TO_CELCIUS}.')
            return FAHRENHEIT_TO_CELCIUS   

        print(f'Invalid conversion option "{choice}" selected. Expecting 1 or 2.')
        logger.warning(f'Invalid conversion option "{choice}" selected. Expecting 1 or 2.')


def get_temperature():
    ''' 
    Get the temperature value to be converted.

    Returns:
            float: Converted temperature value.
    '''
    logger.info('Getting temperature value for conversion.')
    while True:
        try:
            temperature = float(input("\nEnter temperature value (0 to quit):"))

            if temperature == 0:
                exit_program(EXIT_MESSAGE)

            print(f'Temperature entered is: {temperature}.')
            logger.info(f'Temperature entered is: {temperature}.')
            return temperature

        except ValueError as ex:
            print('Invalid number entered for temperature.' + '\n' + 'Please enter a valid numeric value.')
            logger.warning('Invalid number entered for temperature.' + '\n' + f'Please enter a valid numeric value. \n{ex}')


def perform_conversion(temperature, conversion_type_code=CELCIUS_TO_FAHRENHEIT):
    '''
    Perform temperature conversion of the specified temperature value and conversion code.

    Args:
            temperature (float): Temperature to be converted to another unit.
    Returns:
            float: Converted temperature.
    '''
    if not isinstance(temperature, float):
        raise ValueError(f'Invalid type for temperature. Expected a float.')

    if conversion_type_code == CELCIUS_TO_FAHRENHEIT:
        converted_temperature = ((temperature * 1.8) + 32)

        print(f'Result: {temperature}°C is: {converted_temperature}°F.')
        logger.info(f'Result: {temperature}°C is: {converted_temperature}°F.')
        return converted_temperature

    if conversion_type_code == FAHRENHEIT_TO_CELCIUS:
        converted_temperature = ((temperature - 32) / 1.8)

        print(f'Result: {temperature}°F is: {converted_temperature}°C.')
        logger.info(f'Result: {temperature}°F is: {converted_temperature}°C.')
        return converted_temperature

    # raise exception if no match conversion type was found
    raise tempconv_error.ConversionTypeCodeError('Invalid conversion type code entered.')

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
        print("Welcome to TEMPERATURE CONVERTER")

        while True:
            try:
                conversion_type = get_conversion_type()
                temperature = get_temperature()

                perform_conversion(temperature, conversion_type)

            except ValueError as ex:
                print(f'{INVALID_INPUT}: {ex}')
                logger.warning(f'{INVALID_INPUT}: {ex}')

            except tempconv_error.ConversionTypeCodeError as ex:
                print(f'Conversion Type Code Issue: {ex}')
                logger.warning(f'Conversion Type Code Issue: {ex}')

    except Exception as ex:
        logger.exception("Error occured in main temperature conversion function.")


if __name__ == "__main__":
    main()