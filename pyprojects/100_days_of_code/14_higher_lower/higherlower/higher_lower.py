'''
Create the higher lower game, guess from among two options
which has the higher value.

@datetime:: March 2, 2025 11:49 pm (UTC-5)
@author:: jac0der
'''
import sys
import art
from random import sample
from game_data import data
from higher_lower_error import HigherLowerError
import higher_lower_constants as hlc
from logging_custom import jaclog

logger = jaclog.configure('higher_lower', './higher_lower.log')


def print_logo()->None:
    """ Prints the logo for the game. """
    print(art.logo)


def print_vs()->None:
    """ Prints the VS symbol for the game coparissions. """
    print(art.vs)


def increment_score()->None:
    """ """
    logger.info("")
    hlc.SCORE += 1


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


def display_comparissions(compare:str, against:str)->None:
    '''
    Displays to the user the comparission match up for two randomly selected items.

    Args:
            compare (str): The first game data item to be compared with another.
            against (str): The second game dat item the first item is compared against.
    '''
    print(compare)
    print_vs()
    print(against)


def get_user_choice()->str:
    '''
    Accepts the user comparisson choice.

    Returns:
            str: The user's comparisson choice.
    '''
    logger.info("  user's comparisson choice.")

    while True:
        choice = input(hlc.FOLLOWER_PROMPT).strip().lower()

        if choice == hlc.CHOICE_A:
            return hlc.CHOICE_A
        elif choice == hlc.CHOICE_B:
            return hlc.CHOICE_B
        else:
            logger.warning(hlc.USER_CHOICE_WARNING)
            print(hlc.USER_CHOICE_WARNING)


def init_compare()->dict:
    ''' 
    '''
    logger.info("")

    data_items = get_compare_item(data, hlc.INITIAL_DATA_SELECT)
    compare_item = data_items[0]
    against_item = data_items[1]
    logger.info(f"compare item: {compare_item}")
    logger.info(f"against item: {against_item}")

    compare_item_line = formulate_comparisson_line(hlc.TAG_A, compare_item)
    logger.info(f"compare_item_line is: {compare_item_line}")

    against_item_line = formulate_comparisson_line(hlc.TAG_B, against_item)
    logger.info(f"against_item_line is: {against_item_line}")

    display_comparissions(compare_item_line, against_item_line)

    choice = get_user_choice()



    return against_item


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

        compare_item = init_compare()
        
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