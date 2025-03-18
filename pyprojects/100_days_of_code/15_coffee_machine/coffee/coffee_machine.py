'''
Create a digital coffee simulation machine used to create 
coffee for customers.

@datetime:: March 17, 2025 1:06 am (UTC-5)
@author:: jac0der
'''

from art import logo
import coffee_data as cd
from logging_custom import jaclog
import coffee_machine_constants as cmc

logger = jaclog.configure('coffee_machine', './coffee_machine.log')


def display_logo()->None:
    """ Prints the logo for the Coffee Machine program. """
    logger.info("Printing coffee logo art.")
    print(logo)


def coffee_order()->str:
    '''
    Gets the type of coffee customer ordered to be made.

    Returns:
            str: The type of coffee customer ordered.
    '''
    logger.info("Getting customer coffee order.")

    coffee_order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    print(cmc.COFFEE_ORDER.format(coffee_order))
    logger.info(cmc.COFFEE_ORDER.format(coffee_order))
    return coffee_order


def main()->None:
    """ Main function to start the Coffee Machine Program. """
    try:
        logger.info("Starting the coffee machine program.")
        display_logo()
        coffee_order()
    
    except (KeyboardInterrupt, EOFError):
        print(f"\n{cmc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Coffee Machine function.")


if __name__ == "__main__":
    main()