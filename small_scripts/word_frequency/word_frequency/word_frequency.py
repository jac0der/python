'''
Word Frequency. Count the amount of words in a given sequence
of string or sentence.

@datetime:: February 14, 2025 11:26 pm (UTC-5)
@author:: jac0der
'''
import sys
import os
import word_frequency_constants as wfc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('word_frequency', './word_frequency.log')


def get_text()->str:
    """ 
    Get the text input to count the word occurence. Text is trimmed at start
    and end.
    """
    logger.info("Retrieving text input for word count.")
    return input("Enter text: ").strip()



def exit_program(message, code=0)->None:
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)


def main()->None:
    """ Main function to start the Word Frequency program. """
    try:
        logger.info('Starting Word Frequency Program.')
        get_text()
    
    except (KeyboardInterrupt, EOFError):
        print(f"\n{wfc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main BlackJack function.")


if __name__ == "__main__":
    main()
