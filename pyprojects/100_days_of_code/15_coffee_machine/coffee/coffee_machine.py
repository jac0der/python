'''
Create a digital coffee simulation machine used to create 
coffee for customers.

@datetime:: March 17, 2025 1:06 am (UTC-5)
@author:: jac0der
'''

import sys
import typing
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

    for key, value in coffee_machine_resources.items():
        
        if key != "money":

            if key in ['water', 'milk']:
                unit = 'ml'
            elif key == 'coffee':
                unit = 'g'

            print(f"{key.title()}: {value}{unit}")
        else:
            unit = '$'
            print(f"{key.title()}: {unit}{value}")

    print("\n")


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


def coffee_order()->dict[str,typing.Any]:
    '''
    Gets the type of coffee customer ordered to be made.

    Returns:
            dict: The customer's coffee order - ingredients used to make the order and cost. 
    '''
    logger.info("Getting customer coffee order.")

    while True:
        try:
            coffee_order = input("What would you like? (espresso/latte/cappuccino) (off to quit): ").strip().lower()

            if coffee_order == cmc.EXIT_TRIGGER:
                exit_program(cmc.EXIT_MESSAGE, 0)

            if coffee_order == cmc.REPORT_TRIGGER:
                generate_resources_report(cd.resources)
                continue

            coffee_item:dict = validate_coffee_order(coffee_order, cd.MENU)

            if len(coffee_item) > 0:
                break
            else:
                print(cmc.ORDER_VALIDATION_WARNING.format(coffee_order))
                logger.warning(cmc.ORDER_VALIDATION_WARNING.format(coffee_order))
    
        except cme.CoffeeMachineError as ex:
            logger.warning(f"CoffeeMachineError: {ex}")

    cmc.ORDERED_COFFEE = coffee_order
    logger.info(cmc.COFFEE_ORDER.format(coffee_order, coffee_item))
    return coffee_item


def check_coffee_machine_resources(ordered_coffee:dict[str,int], coffee_machine:dict[str,int])->str:
   '''
    Check if coffee machine has sufficient ingredient resources to make the customer's
    coffee order.

    Args:
            ordered_coffee (dict[str,int]): The coffee order of customer.
            coffee_machine (dict[str,int]): The coffee machine current available ingredient amounts.
    Returns:
            str: The first insufficient coffee ingredient from the current coffee machine ingredient amounts.
   '''
   logger.info(f"Checking if coffee machine has sufficient ingredients to make '{ordered_coffee}'")

   if not isinstance(ordered_coffee, dict) or not isinstance(coffee_machine,dict):
        raise TypeError(f"Invalid Type for ordered_coffee or coffee_machine. Expected a dictionary value.")

   if len(ordered_coffee) == 0 or len(coffee_machine) == 0:
        raise cme.CoffeeMachineError(f"Invalid Input: 'ordered_coffee' or 'coffee_machine' parameters cannot be empty.")

   for ingredient, ingredient_amount in ordered_coffee.items():
        if ingredient_amount > coffee_machine[ingredient]:
            return ingredient

   return ""


def get_coin_total(coin_amounts:dict[str,int], coffee_machine_coins:dict[str,float])->float:
    '''
    Calculate the total coins dollar value entered by customer
    to pay for their coffee order.

    Args:
            coin_amounts (dict[str,int]): The total amount of coins enetred by customer for
                                          each coin (quarter, dime etc...)
            
            coffee_machine_coins (dict[str,float]): The coffee machine coins dollar value associations.
                                                    Ex. quarters: 0.25, dimes: 0.10 etc...
    Returns:
            float: Calculated dollar value for amount of coins entered into coffee machine.
    '''
    logger.info(f"Tallying coins total for {coin_amounts}.")

    if not isinstance(coin_amounts, dict):
        raise TypeError(f"Invalid Type for coin_amounts. Expected a dictionary value.")

    if len(coin_amounts) == 0:
        raise cme.CoffeeMachineError(f"Invalid Input: 'coin_amounts' parameter cannot be empty.")

    total:float = 0

    for coin, coin_amount in coin_amounts.items():
        total = total + (coin_amount * coffee_machine_coins[coin])

    logger.info(f"Coin dollar value: {total}.")
    return total


def update_coffee_machine()->None:
    pass


def process_payment(ordered_coffee:dict[str,typing.Any])->None:
    '''
    Process the payment for coffee in coins.

    Args:
            ordered_coffee (dict[str,typing.Any]): The customer's coffee order being paid for.
    '''
    logger.info(f"Processing payment for '{ordered_coffee}'")

    if not isinstance(ordered_coffee, dict):
        raise TypeError(f"Invalid Type for ordered_coffee. Expected a dictionary value.")

    if len(ordered_coffee) == 0:
        raise cme.CoffeeMachineError(f"Invalid Input: 'ordered_coffee' parameter cannot be empty.")

    print("Please insert coins.")

    coin_entry:bool = True
    coin_amounts:dict = dict()

    for coin in cmc.COINS.keys():

        while coin_entry:
            try:
                coin_amount = int(input(f"How many {coin}?: ").strip())

                if coin_amount < 0:
                    raise cme.CoffeeMachineError(cmc.COIN_AMOUNT_NUMBER_WARNING.format(coin))

                coin_amounts[coin] = coin_amount
                coin_entry = False

            except ValueError as ex:
                print(cmc.COIN_AMOUNT_WARNING.format(coin))
                logger.warning(cmc.COIN_AMOUNT_WARNING.format(coin))
            
            except cme.CoffeeMachineError as ex:
                print(cmc.COIN_AMOUNT_NUMBER_WARNING.format(coin))
                logger.warning(f"CoffeeMachineError: {ex}")

        coin_entry = True
    
    logger.info(f"coin_amounts is: {coin_amounts}")
    print(coin_amounts)

    dollar_value = get_coin_total(coin_amounts, cmc.COINS)
    print(dollar_value)

    coffee_cost:float = ordered_coffee['cost']
    logger.info(f"Cost for {cmc.ORDERED_COFFEE}: ${coffee_cost}")

    if dollar_value < coffee_cost:
        print(cmc.INSUFFICIENT_FUNDS.format(cmc.ORDERED_COFFEE))
        logger.info(cmc.INSUFFICIENT_FUNDS.format(cmc.ORDERED_COFFEE))
        return

    elif dollar_value > coffee_cost:
        change:float = dollar_value - coffee_cost

        print(cmc.ORDER_CHANGE.format(round((change),2)))
        logger.info(cmc.ORDER_CHANGE.format(round((change),2)))

    print(cmc.ORDER_SUCCESS.format(cmc.ORDERED_COFFEE), end='\n\n')
    logger.info(cmc.ORDER_SUCCESS.format(cmc.ORDERED_COFFEE))
        

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
        
        while True:                        
            ordered_coffee:dict[str, typing.Any] = coffee_order()

            sufficient_ingredients:str = check_coffee_machine_resources(ordered_coffee['ingredients'], cd.resources)

            if len(sufficient_ingredients) > 0:
                print(f"Sorry there is not enough {sufficient_ingredients}")

            process_payment(ordered_coffee)

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except cme.CoffeeMachineError as ex:
        logger.error(f"CoffeeMachineError: {ex}")
   
    except (KeyboardInterrupt, EOFError):
        print(f"\n{cmc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Coffee Machine function.")


if __name__ == "__main__":
    main()