'''
    Create a reusable logging module to be used throughout my python applications.

    @datetime:: February 02, 2025 6:05 am (UTC-5)
    @author:: jacoder
'''
import logging
from logging.handlers import RotatingFileHandler


def configure(logger_name, log_file, log_formatter = "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"):
    '''
        Function use to set up the logger.

        Args:
                logger_name (string): name of the logger.
                log_file (str): full path and name of the file to be used
                                to write log messages to.
                log_formatter (str): default parameter used to specify the format of the
                                     log messages.
        Returns:
                logger: loger object writting log messages.
    '''
    # Create a logger with name logger_name
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # Set the base logging level for the logger

    # Prevent duplicate handlers
    if not logger.handlers:
        # Create a file handler (for DEBUG and above)
        #file_handler = logging.FileHandler(log_file)
        file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)

        # DEBUG, INFO, WARNING, ERROR, and CRITICAL messages go to the file
        file_handler.setLevel(logging.DEBUG)  

        # Create a formatter
        formatter = logging.Formatter(log_formatter)

        # Add the formatter to the handler
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)

        '''# Console handler for real-time output
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        '''

    return logger
