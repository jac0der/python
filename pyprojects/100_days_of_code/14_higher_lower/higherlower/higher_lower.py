'''
Create the higher lower game, guess from among two options
which has the higher value.

@datetime:: March 2, 2025 11:49 pm (UTC-5)
@author:: jac0der
'''
import art
from random import sample
from game_data import data
import higher_lower_constants as hlc
from logging_custom import jaclog

logger = jaclog.configure('number_guess', './number_guess.log')


def print_logo()->None:
    """ Prints the logo for the game. """
    print(art.logo)


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

    logger.info(f"Retrieving {item_amount} game data for comparisson.")
    return sample(game_data, item_amount)


def main()->None:
    """ Main function to start the Higher Lower Program. """
    try:
        logger.info("Starting the Higher Lower Game.")
        print_logo()

        data_items = get_compare_item(data, hlc.INITIAL_DATA_SELECT)
        compare_item = data_items[0]
        against_item = data_items[1]
        logger.info(f"compare item: {compare_item}")
        logger.info(f"against item: {against_item}")

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{hlc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Higher Lower function.")


if __name__ == "__main__":
    main()