'''
    Program to calculate amounts payable by a number
    of patrons or friends from a bill, inclusive of
    a percentage tip added to bill total.

    @datetime:: September 18, 2024 5:14 am (UTC-5)
    @author:: jacoder
'''
import sys
import tip_calculator_constants as tcc
from logging_custom import jaclog

logger = jaclog.configure('tip_calculator', './tip_calculator.log')


def get_bill_amount(message:str)->float:
    '''
    Get the bill amount from user, and validate to ensure it is a valid
    numeric float entry.

    Args:
            message (str): The text to display when asking user for input.

    Returns:
            float: The validated bill amount. 
    '''
    logger.info("Getting bill amount.")

    if not isinstance(message, str):
        raise TypeError(f"Invalid Input: Expected Type 'str' for message '{message}' parameter.")

    while True:
        try:
            bill:float = float(input(message))

            if str(int(bill)) == tcc.EXIT_TRIGGER:
                exit_program(tcc.EXIT_MESSAGE, 0)

            logger.info(f"Bill amount: {bill}")

            return bill
        
        except ValueError as ex:
            print(tcc.GET_NUMBER_WARNING.format(tcc.BILL_AMOUNT))
            logger.warning(f'{tcc.GET_NUMBER_WARNING.format(tcc.BILL_AMOUNT)} \n {ex}')


def get_input(message:str, is_tip:bool=False)->int:
    '''
    Get the percentage tip or amount of patron to split bill among from user, and validate to 
    ensure it is a valid numeric int entry.

    Args:
            message (str): The text to display when asking user for input.

    Returns:
            int: The validated tip percentage or patron count. 
    '''
    logger.info("Getting tip percentage or patron count.")

    if not isinstance(message, str):
        raise TypeError(f"Invalid Input: Expected Type 'str' for message '{message}' parameter.")

    while True:
        try:
            user_input:int = int(input(message))

            if str(user_input) == tcc.EXIT_TRIGGER:
                exit_program(tcc.EXIT_MESSAGE, 0)

            if is_tip:
                if user_input not in tcc.TIP_PERCENTAGES:
                    print(tcc.TIP_PERCENTAGES_WARNING.format(user_input))
                    logger.warning(tcc.TIP_PERCENTAGES_WARNING.format(user_input))
                    continue

            return user_input
        
        except ValueError as ex:
            print(tcc.GET_NUMBER_WARNING.format(tcc.TIP_PATRON))
            logger.warning(f'{tcc.GET_NUMBER_WARNING.format(tcc.TIP_PATRON)} \n {ex}')


def calculate_pay_amounts()->float:
    '''
    Function to calculate and split up how much each of a number of 
    friends/patron is to pay from a bill.

    Returns:

        float: Amount payable by each patron.
    '''   
    logger.info("Calculating payable amounts.")
    
    bill:float = get_bill_amount("What was the total bill? (0 to quit) $")
    bill:float = get_bill_amount("What was the total bill? (0 to quit) $")

    tip:int = get_input("What percentage tip would you like to give? (0 to quit) 10, 12, or 15? ", True)
    logger.info(f"Tip: {tip}")

    people:int = get_input("How many people to split the bill? (0 to quit) ")
    people:int = get_input("How many people to split the bill? (0 to quit) ")
    logger.info(f"People: {people}")

    # bill total plus added tip percentage
    grand_total:float = bill + (bill * (tip/100))
    grand_total:float = bill + (bill * (tip/100))
    logger.info(f"Grand Total: {grand_total}")

    # At this point, people cannot be 0 due to prior EXIT_TRIGGER check
    split_amount:float = round((grand_total / people), 2)

    return split_amount


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
    """ Main function to start the Tip Calculator Program. """
    try:
        logger.info("Starting the Tip Calculator Program.")

        print("Welcome to the tip calculator!")
        split_amount:float = calculate_pay_amounts()
        split_amount:float = calculate_pay_amounts()

        print(tcc.RESULT_MESSAGE.format(split_amount))
        logger.info(tcc.RESULT_MESSAGE.format(split_amount))

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{tcc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main Tip Calculator function.")


if __name__ == "__main__":
    main()