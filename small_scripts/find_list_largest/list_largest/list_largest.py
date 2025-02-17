'''
    Find the largest number within a list

    @datetime:: February 16, 2025 11:18 pm (UTC-5)
    @author:: jac0der
'''
from logging_custom import jaclog
import list_largest_constants as llc

logger = jaclog.configure('list_largest', './list_largest.log')


def get_largest_item(list_items:list[int])->int:
    """
    Returns the largest number from a given list of numbers.

    Args:
            list_items (list[int]): The list of numbers from which to pick the largest
                                    number to return.
    Returns:
            int: The largest number within the list_items argument.
    """
    return max(list_items)


def process_list_collection(collection:list[list[int]])->None:
    """
    Prints the largest numbers from each list of numbers within a specified list collection.

    Args:
            collection (list[list[int]]): The list collection comprising of a list of list of numbers.
    """
    largest_item_lines = [f"Largest number in {list} is: {get_largest_item(list)}" for list in collection]
    result = "\n".join(largest_item_lines)
    print(result)


def main()->None:
    """ Main function to start the Largest List Item program.  """
    try:
        logger.info('Starting the largest list item program.')
        process_list_collection(llc.LIST_COLLECTION)
        
    except (KeyboardInterrupt, EOFError):
        print(f"\n{llc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Find Largest List Item function.")


if __name__ == "__main__":
    main()






