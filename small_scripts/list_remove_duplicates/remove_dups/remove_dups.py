'''
    Remove duplicates from a list.

    @datetime:: February 19, 2025 11:29 pm (UTC-5)
    @author:: jac0der
'''
from logging_custom import jaclog
import remove_dups_constants as rdc
from typing import Any

logger = jaclog.configure('list_remove_dups', './list_remove_dups.log')


def remove_duplicates(list_items:list[Any])->list[Any]:
    '''
    Remove duplicate items from a list.

    Args:
            list_items (list[any]): List of duplicated items, no specific data type.
    Returns:
            list[any]: List of unique items.
    '''
    if not isinstance(list_items, list):
        raise TypeError("Invalid Type: Expecting list for list_items parameter.")

    logger.info("Removing duplicates from list.")
    seen = set()
    return [x for x in list_items if not (x in seen or seen.add(x))]


def process_duplicates(collection:list[list[Any]])->None:
    '''
    Process a collection of lists, removing duplicates from each list within the
    collection of lists.

    Args:
            collection (list[list[any]]): A collection of lists to remove duplicates from.
    '''
    if not isinstance(collection, list):
        raise TypeError("Invalid Type: Expecting list for collection parameter.")

    logger.info("Processing list collection.")

    unique_lists = [f"{remove_duplicates(inner_list)}" for inner_list in collection]
    result = "\n".join(map(str, (remove_duplicates(inner_list) for inner_list in collection)))
    #result = "\n".join(unique_lists)
    print(result)


def main()->None:
    """ Main function to start the Remove Duplicates program """
    try:
        logger.info('Starting the remove dupliates program.')
        process_duplicates(rdc.LIST_COLLECTION)

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")
    
    except (KeyboardInterrupt, EOFError):
        print(f"\n{rdc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Remove Duplicates function.")


if __name__ == "__main__":
    main()