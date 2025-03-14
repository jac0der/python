''' 
    Program to convert from Celsius to Fahrenheit or, Fahrenheit to Celsius.

    @datetime:: February 8, 2025 2:42 am (UTC-5)
    @author:: jac0der
'''
import os 
import sys
import tempconv_error
import tempconv_constants as tc
from logging_custom import jaclog
from tempconv_enum import ConversionType

logger = jaclog.configure('temperature_convertor', './tempconv.log')


CONVERSIONS = {
    ConversionType.CELSIUS_TO_FAHRENHEIT: lambda t: (t * 1.8) + 32,
    ConversionType.FAHRENHEIT_TO_CELSIUS: lambda t: (t - 32) / 1.8
}


def get_conversion_type()->None:
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
        choice = input('\nChoose conversion type (0 to quit): ')

        if choice == '0':
            exit_program(tc.EXIT_MESSAGE, 0)

        if choice == '1':
            logger.info(f'Conversion type is: {ConversionType.CELSIUS_TO_FAHRENHEIT}.')
            return ConversionType.CELSIUS_TO_FAHRENHEIT

        if choice == '2':
            logger.info(f'Conversion type is: {ConversionType.FAHRENHEIT_TO_CELSIUS}.')
            return ConversionType.FAHRENHEIT_TO_CELSIUS   

        print(tc.CONVERSION_TYPE_WARNING.format(choice))
        logger.warning(tc.CONVERSION_TYPE_WARNING.format(choice))


def get_temperature()->None:
    ''' 
    Get the temperature value to be converted.

    Returns:
            float: Converted temperature value.
    '''
    logger.info('Getting temperature value for conversion.')
    while True:
        try:
            user_input = input("\nEnter temperature value (q to quit): ")
            if user_input.lower().strip() == 'q':
                exit_program(tc.EXIT_MESSAGE, 0)

            temperature = float(user_input)

            print(tc.TEMPERATURE_MESSAGE.format(temperature))
            logger.info(tc.TEMPERATURE_MESSAGE.format(temperature))
            return temperature

        except ValueError as ex:
            print(tc.GET_TEMPERATURE_WARNING)
            logger.warning(f'{tc.GET_TEMPERATURE_WARNING} \n {ex}')


def perform_conversion(temperature:float, conversion_type_code:str=ConversionType.CELSIUS_TO_FAHRENHEIT)->float:
    '''
    Perform temperature conversion of the specified temperature value and conversion code.

    Args:
            temperature (float): Temperature to be converted to another unit.
    Returns:
            float: Converted temperature.
    '''
    logger.info('Start performing temperature conversion.')
    if not isinstance(temperature, (int,float)):
        raise ValueError(f'Invalid type for temperature. Expected a numeric value.')

    try:
        converted_temperature = CONVERSIONS[conversion_type_code](temperature)

        print(f'Result: {temperature}° → {converted_temperature}°.')
        logger.info(f'Converted {temperature}° to {converted_temperature}° using {conversion_type_code}.')
        return converted_temperature

    except KeyError:
        # raise exception if no match conversion type was found
        raise tempconv_error.ConversionTypeCodeError("Invalid conversion type code entered.")


def exit_program(message:str, code:int=0)->None:
    '''
    Centralized exit function to handle program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    print(message)
    sys.exit(code)


def main()->None:
    """ Main function to start the Temperature Conversion Program. """
    try:
        logger.info("Starting Temperature Converter.")
        print("Welcome to TEMPERATURE CONVERTER")

        while True:
            try:
                conversion_type = get_conversion_type()
                temperature = get_temperature()

                perform_conversion(temperature, conversion_type)

            except ValueError as ex:
                print(f"{tc.INVALID_INPUT}: {ex}")
                logger.warning(f"{tc.INVALID_INPUT}: {ex}")

            except tempconv_error.ConversionTypeCodeError as ex:
                print(f"{tc.CONVERSION_ISSUE} \n {ex}")
                logger.warning(f"{tc.CONVERSION_ISSUE} \n {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{tc.EXIT_MESSAGE}")
        return

    except Exception as ex:
        logger.exception("Error occurred in main Temperature Conversion Function.")


if __name__ == "__main__":
    main()