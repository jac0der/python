'''
    Create a reusable exit module to be used throughout my python applications.

    @datetime:: June 10, 2026 6:49 am (UTC-5)
    @author:: jacoder
'''
import sys


def exit_program(message:str, logger:Logger, code:int=0)->None:
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)