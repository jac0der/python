'''
Create a digital coffee simulation machine used to create 
coffee for customers.

@datetime:: March 17, 2025 1:06 am (UTC-5)
@author:: jac0der
'''

from art import logo
import coffee_data as cd
from logging_custom import jaclog
import coffee_machine_error as cme
import coffee_machine_constants as cmc

logger = jaclog.configure('coffee_machine', './coffee_machine.log')


def display_logo()->None:
    """ Prints the logo for the Coffee Machine program. """
    logger.info("Printing coffee logo art.")
    print(logo)


def validate_coffee_order(coffee_order:str, menu:dict[str,dict])->bool:
    '''
    Validating the coffee order to ensure customer's coffee order
    is on the coffee menu.

    Args:
            coffee_order (str): The customer's coffee order.
            menu (dict[str,dict]): The coffee menu from which customer makes order.
    Returns:
            bool: True customer's coffee order is on the coffee menu,
                  otherwise False.
    '''
    logger.info("Validating coffee order.")
    if not isinstance(coffee_order, str):
        raise TypeError(f"Invalid Type for 'coffee_order': Expected a string value.")

    if not isinstance(menu, dict):
        raise TypeError(f"Invalid Type for 'menu': Expected a dictionary value.")

    if len(coffee_order) == 0 or len(menu) == 0:
        raise cme.CoffeeMachineError(f"Invalid Input: 'coffee_order' or 'menu' parameters cannot be empty.")

    coffee_item = menu.get(coffee_order)

    if coffee_item is None:
        return False

    return True


def coffee_order()->str:
    '''
    Gets the type of coffee customer ordered to be made.

    Returns:
            str: The type of coffee customer ordered.
    '''
    logger.info("Getting customer coffee order.")

    while True:
        try:
            coffee_order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
            if validate_coffee_order(coffee_order, cd.MENU):
                break
            else:
                print(cmc.ORDER_VALIDATION_WARNING.format(coffee_order))
                logger.warning(cmc.ORDER_VALIDATION_WARNING.format(coffee_order))
    
        except cme.CoffeeMachineError as ex:
            logger.warning(f"CoffeeMachineError: {ex}")

    print(cmc.COFFEE_ORDER.format(coffee_order))
    logger.info(cmc.COFFEE_ORDER.format(coffee_order))
    return coffee_order


def main()->None:
    """ Main function to start the Coffee Machine Program. """
    try:
        logger.info("Starting the coffee machine program.")
        display_logo()
        coffee_order()

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")
   
    except (KeyboardInterrupt, EOFError):
        print(f"\n{cmc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Coffee Machine function.")


if __name__ == "__main__":
    main()