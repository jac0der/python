'''
Word Frequency. Count the amount of words in a given sequence
of string or sentence.

@datetime:: February 14, 2025 11:26 pm (UTC-5)
@author:: jac0der
'''
import sys
import os
from logging_custom import jaclog
import word_frequency_error as wfe
import word_frequency_constants as wfc

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

    if not isinstance(text, str):
        raise TypeError("Invalid input, Expected Type str for input 'text'.")

    if len(text.strip()) == 0:
        raise wfe.WordFrequencyError("Invalid input, text cannot be empty.")

    return text.split(" ")


def get_unique_items(words: list[str])->set[str]:
    '''
    Separate the unique words from the words list.
    Raise WordFrequencyError if the words list is empty.

    Args:
            words (list[str]): The list of word items from which to pull only unique words.
    Returns:
            set[str]: The unique Set of words from the words list
    '''
    logger.info("Pulling unique items from words list.")

    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise TypeError('Invalid Type: words must be a list of strings.')

    if len(words) == 0:
        raise wfe.WordFrequencyError("Invalid input, words list cannot be empty.")

    return set(words)


def generate_word_tally(unique_words: set[str], words: list[str])->dict[str, int]:
    '''
    Generate the word tally for each unique word in the words list.

    Args:
            unique_words (set[str]): All the unique words from the words list.
            words (list[str]): All the words retrieved from the input.
    Returns:
            dict(): A dictionary storing each word as key and the word occurence in the
                    words list as the value.
    '''
    logger.info('Generating word tally.')

    if not isinstance(unique_words, set) or not isinstance(words, list):
        raise TypeError('Invalid Type: Expected set[str] for unique_words and list[str] for words arguments.')

    if len(unique_words) == 0 or len(words) == 0:
        raise wfe.WordFrequencyError("Invalid input: Expected non-empty set 'unique_words' and non-empty list 'words'.")

    return {
        unique_word:words.count(unique_word) 
        for unique_word in unique_words 
        if len(unique_word.strip()) > 0
    }

   
def exit_program(message:str, code=0)->None:
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    print(message)
    sys.exit(code)


def main()->None:
    """ Main function to start the Word Frequency program. """
    try:
        logger.info('Starting Word Frequency Program.')
        
        words = formulate_word_list(get_text())
        print(wfc.TOTAL_WORDS.format(len(words)))
        logger.info(wfc.TOTAL_WORDS.format(len(words)))

        unique_words: set[str] = get_unique_items(words)
        print(wfc.UNIQUE_WORDS.format(unique_words))
        logger.info(wfc.UNIQUE_WORDS.format(unique_words))

        word_tally = generate_word_tally(unique_words, words)
        print(wfc.WORD_TALLY.format(word_tally))
        logger.info(wfc.WORD_TALLY.format(word_tally))

    except KeyError as ex:
        logger.error(f"KeyError: {ex}")

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

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
