'''
Create a digital coffee simulation machine used to create 
coffee for customers.

@datetime:: March 17, 2025 1:06 am (UTC-5)
@author:: jac0der
'''

import coffee_machine_constants as cmc
from logging_custom import jaclog

logger = jaclog.configure('coffee_machine', './coffee_machine.log')


def main()->None:
    """ Main function to start the Coffee Machine Program. """
    try:
        logger.info("Starting the coffee machine program.")
    
    except (KeyboardInterrupt, EOFError):
        print(f"\n{cmc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Coffee Machine function.")


if __name__ == "__main__":
    main()