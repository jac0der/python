'''
Create a digital coffee simulation machine used to create 
coffee for customers.

@datetime:: March 17, 2025 1:06 am (UTC-5)
@author:: jac0der
'''

import sys
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


def generate_resources_report(coffee_machine_resources:dict[str, int])->None:
    '''
    Generates a current resource details report for the coffee machine.

    Args:
            coffee_machine_resources (dict[str, int]): The coffee machine for which to print the 
                                                       current available coffee resources to make coffee.
    '''
    logger.info("Generating current coffee machine resources report.")

    if not isinstance(coffee_machine_resources, dict):
        raise TypeError(f"Invalid Type for 'coffee_machine_resources': Expected a dictionary value.")

    if len(coffee_machine_resources) == 0:
        raise cme.CoffeeMachineError(f"Invalid Input: 'coffee_machine_resources' parameter cannot be empty.")

    print(f"Water: {coffee_machine_resources.get("water")}ml")
    print(f"Milk: {coffee_machine_resources.get("milk")}ml")
    print(f"Coffee: {coffee_machine_resources.get("coffee")}g", end='\n\n')


def validate_coffee_order(coffee_order:str, menu:dict[str,dict])->dict:
    '''
    Validating the coffee order to ensure customer's coffee order
    is on the coffee menu.

    Args:
            coffee_order (str): The customer's coffee order.
            menu (dict[str,dict]): The coffee menu from which customer makes order.
    Returns:
            dict: The customer's coffee order - ingredients used to make the order and cost. 
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
        return {}

    return coffee_item


def coffee_order()->dict:
    '''
    Gets the type of coffee customer ordered to be made.

    Returns:
            dict: The customer's coffee order - ingredients used to make the order and cost. 
    '''
    logger.info("Getting customer coffee order.")

    while True:
        try:
            coffee_order = input("What would you like? (espresso/latte/cappuccino) (q to quit): ").strip().lower()

            if coffee_order == cmc.EXIT_TRIGGER:
                exit_program(cmc.EXIT_MESSAGE, 0)

            if coffee_order == cmc.REPORT_TRIGGER:
                generate_resources_report(cd.resources)
                continue

            coffee_item = validate_coffee_order(coffee_order, cd.MENU)

            if len(coffee_item) > 0:
                break
            else:
                print(cmc.ORDER_VALIDATION_WARNING.format(coffee_order))
                logger.warning(cmc.ORDER_VALIDATION_WARNING.format(coffee_order))
    
        except cme.CoffeeMachineError as ex:
            logger.warning(f"CoffeeMachineError: {ex}")

    print(cmc.COFFEE_ORDER.format(coffee_order, coffee_item))
    logger.info(cmc.COFFEE_ORDER.format(coffee_order, coffee_item))
    return coffee_item


def exit_program(message:str, code:int=0)->None:
    '''
    Centralized exit function to handle program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    print(message)
    sys.exit(code)


def main()->None:
    """ Main function to start the Coffee Machine Program. """
    try:
        logger.info("Starting the coffee machine program.")
        display_logo()
        coffeeorder = coffee_order()

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")
   
    except (KeyboardInterrupt, EOFError):
        print(f"\n{cmc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Coffee Machine function.")


if __name__ == "__main__":
    main()