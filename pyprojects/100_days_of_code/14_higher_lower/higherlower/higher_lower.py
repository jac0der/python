'''
Create the higher lower game, guess from among two options
which has the higher value.

@datetime:: March 2, 2025 11:49 pm (UTC-5)
@author:: jac0der
'''
import sys
import art
import os
from random import sample
from game_data import data
from higher_lower_error import HigherLowerError
import higher_lower_constants as hlc
from logging_custom import jaclog

logger = jaclog.configure('higher_lower', './higher_lower.log')


def print_logo()->None:
    """ Prints the logo for the game. """
    logger.info("Printing logo art.")
    print(art.logo)


def print_vs()->None:
    """ Prints the VS symbol for the game coparissions. """
    logger.info("Print versus symbol.")
    print(art.vs)


def increment_score()->None:
    """ Increment the score on each successfult guess. """
    logger.info("Incrementing score...")
    hlc.SCORE += 1


def display_score(message:str)->None:
    ''' 
    Clears screen and displays score after each correct guess.
    
    Args:
            message (str): The message to print to the screen to alert user.
    '''
    if not isinstance(message, str):
        raise TypeError(f"Invalid Input: Expected Type 'str' for message {message} parameter.")

    if len(message) == 0:
        raise HigherLowerError(f"Invalid Input: message '{message}' cannot be empty.")

    logger.info("Displaying score...")
    os.system('cls||clear')
    print_logo()
    print(message)


def get_compare_item(game_data:list, item_amount:int)->list[dict]:
    '''
    Retrieves game data item(s) for comparisson.

    Args:
            game_data (list): the list of dictionary items to be used
                              for comparisson within the higher-lower game.
            item_amount (int): The amount of distinct game data items to 
                               randomly select.
    Returns:
            A list containing the randomly selected game data item(s).
    '''
    if not isinstance(game_data, list) or not isinstance(item_amount, int):
        raise TypeError(f"Invalid Input: Expected Type 'list' for game_data {game_data} and 'int' for item_amount {item_amount} parameters.")

    if len(game_data) == 0:
        raise HigherLowerError(f"Invalid Input: Game data list '{game_data}' cannot be empty.")

    if item_amount < 1 or item_amount > 2:
        raise HigherLowerError(f"Invalid Input: item_amount '{item_amount}' parameter must be 1 or 2.")

    logger.info(f"Retrieving {item_amount} game data for comparisson.")
    return sample(game_data, item_amount)


def formulate_comparisson_line(tag:str, comparission_item:dict)->str:
    '''
    Formulates the compare or against message line from the randomly selected
    game data information.

    Args:
            tag (str): A message string to indicate which message is being formulated,
                       whether the first compare message or the against message.
    Returns:
            str: The formulated compare or against message string from the game data item.
    '''
    if not isinstance(tag, str) or not isinstance(comparission_item, dict):
        raise TypeError(f"Invalid Input: Expected Type 'str' for tag '{tag}' parameter and 'dict' for comparission_item '{comparission_item}' parameter.")
    
    if len(tag) == 0:
        raise HigherLowerError(f"Invalid Input: Tag cannot be empty for comparisson line.")

    logger.info(f"Formulating comparisson line for comparisson item '{comparission_item['name']}'")
    return tag + comparission_item['name'] + ", a " + comparission_item['description'] + ", from " + comparission_item['country'] +"."


def display_comparisons(compare_line:str, against_line:str)->None:
    '''
    Displays to the user the comparission match up for two randomly selected items.

    Args:
            compare_line (str): The first game data item to be compared with another.
            against_line (str): The second game dat item the first item is compared against.
    '''
    if not isinstance(compare_line, str) or not isinstance(against_line, str):
        raise TypeError(f"Invalid Input: Expected Type 'str' for compare_line {compare_line} and against_line {against_line} parameters.")

    if len(compare_line) == 0 or len(against_line) == 0:
        raise HigherLowerError(f"Invalid Input: compare_line '{compare_line}' or against_line '{against_line}' cannot be empty.")

    logger.info("Show user the comparission options.")
    print(compare_line)
    print_vs()
    print(against_line)


def get_user_choice()->str:
    '''
    Accepts the user comparisson choice.

    Returns:
            str: The user's comparisson choice.
    '''
    logger.info("Get the user's comparisson choice.")

    while True:
        choice = input(hlc.FOLLOWER_PROMPT).strip().lower()

        if choice == hlc.EXIT_TRIGGER:
            exit_program(hlc.EXIT_MESSAGE, 0)

        if choice == hlc.CHOICE_A.strip().lower():
            logger.info(hlc.USER_CHOICE.format(choice))
            return choice

        elif choice == hlc.CHOICE_B.strip().lower():
            logger.info(hlc.USER_CHOICE.format(choice))
            return choice

        else:
            logger.warning(hlc.USER_CHOICE_WARNING)
            print(hlc.USER_CHOICE_WARNING)


def check_answer(user_choice:str, compare_item_follower_count:int, against_item_follower_count:int)->None:
    '''
    Check whether user's guess is correct or incorrect, based on the follower count for each of the
    game data compare items.

    Args:
            user_choice (str): The user's selection from the two compare options, A or B.
            compare_item_follower_count (int): Total amount of followers for first compare item.
            against_item_follower_count (int): Total amount of followers for the second against item.
    '''
    if not isinstance(user_choice, str) or not isinstance(compare_item_follower_count, int) or \
       not isinstance(against_item_follower_count, int):
        raise TypeError(f"Invalid Input: Expected Type 'str' for user_choice '{user_choice}' and 'int' for compare_item_follower_count '{compare_item_follower_count} and 'int' for against_item_follower_count {against_item_follower_count}.")

    if len(user_choice) == 0:
        raise HigherLowerError(f"Invalid Input: user_choice '{user_choice}' cannot be empty.")

    logger.info("Checking user choice correctness.")

    if (compare_item_follower_count > against_item_follower_count) and user_choice == hlc.CHOICE_A.strip().lower() or \
    (against_item_follower_count > compare_item_follower_count) and user_choice == hlc.CHOICE_B.strip().lower():
        increment_score()
        display_score(hlc.CORRECT_PROMPT.format(hlc.SCORE))
    
    else:
        os.system('cls||clear')
        print_logo()
        exit_program(hlc.INCORRECT_PROMPT.format(hlc.SCORE), 0)


def compare(compare_item:dict, against_item:dict)->dict:
    ''' 
    Compares two data items, giving user the option to chose which of the
    two items has the most followers.
    '''
    logger.info("Comparing data items.")
    logger.info(f"compare item: {compare_item}")
    logger.info(f"against item: {against_item}")

    compare_item_line = formulate_comparisson_line(hlc.TAG_A, compare_item)
    logger.info(f"compare_item_line is: {compare_item_line}")

    against_item_line = formulate_comparisson_line(hlc.TAG_B, against_item)
    logger.info(f"against_item_line is: {against_item_line}")

    display_comparisons(compare_item_line, against_item_line)

    choice = get_user_choice()

    check_answer(choice,  compare_item['follower_count'], against_item['follower_count'])

    return against_item


def init_items()->dict:
    '''
    Retrieves the first two comparisson game data items for comparisson.

    Returns:
            dict: The data item used as the against in the initial guess, which will then be used as the
                  compare item in the next guess. 
    '''
    logger.info("Performing initial comparisson.")

    data_items = get_compare_item(data, hlc.INITIAL_DATA_SELECT)
    compare_item = data_items[0]
    against_item = data_items[1]
    logger.info(f"compare item: {compare_item}")
    logger.info(f"against item: {against_item}")

    return compare(compare_item, against_item)
   

def exit_program(message:str, code:int=0)->None:
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
    """ Main function to start the Higher Lower Program. """
    try:
        logger.info("Starting the Higher Lower Game.")
        print_logo()

        compare_item = init_items()

        while True:
            against_item = get_compare_item(data, 1)[0]
            compare_item = compare(compare_item, against_item)
        
    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except HigherLowerError as ex:
        logger.error(f"HigherLowerError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{hlc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Higher Lower function.")


if __name__ == "__main__":
    main()