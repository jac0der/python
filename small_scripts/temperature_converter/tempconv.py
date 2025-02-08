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


def main():
    try:
        logger.info("Starting Temperature Converter.")
        pass
    except Exception as ex:
        logger.exception("Error occured in main calculator function.")


if __name__ == "__main__":
    main()