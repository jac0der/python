'''
Word Frequency. Count the amount of words in a given sequence
of string or sentence.

@datetime:: February 14, 2025 11:26 pm (UTC-5)
@author:: jac0der
'''
import sys
import os
import word_frequency_error as wfe
import word_frequency_constants as wfc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('word_frequency', './word_frequency.log')


def get_text()->str:
    """ 
    Get the text input to count the word occurences. Text is trimmed at start
    and end.
    """
    logger.info("Retrieving text input for word count.")
    return input("Enter text: ").strip()


def formulate_word_list(text:str)->list[str]:
    """
    Formulate a list of words from the text input. This is achieved by spliting
    the text using a space " " separator, assuming that each word is separated
    by a space. The text is trimmed at start and end from the input step.

    Args:
            text (str): The text sequence from which word tally is counted.
    Returns:
            list[str]: A list of words obtained from spliting the text with space
            separator.
    """
    logger.info("Formulating words list from text input.")

    if len(text.strip()) == 0:
        raise wfe.WordFrequencyError("Invalid input, text cannot be empty.")

    return text.split(" ")


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
        
        words = formulate_word_list(get_text())
        print(wfc.TOTAL_WORDS.format(len(words)))
        logger.info(wfc.TOTAL_WORDS.format(len(words)))

    except wfe.WordFrequencyError as ex:
        print(f"WordFrequencyError: {ex}")
        logger.error(f"WordFrequencyError: {ex}")
    
    except (KeyboardInterrupt, EOFError):
        print(f"\n{wfc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Word Frequency function.")


if __name__ == "__main__":
    main()
