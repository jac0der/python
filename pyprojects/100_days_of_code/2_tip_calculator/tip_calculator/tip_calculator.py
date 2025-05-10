'''
    Program to calculate amounts payable by a number
    of patrons or friends from a bill, inclusive of
    a percentage tip added to bill total.

    @datetime:: September 18, 2024 5:14 am (UTC-5)
    @author:: jacoder
'''
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

    while True:
        try:
            bill = float(input(message))
            logger.info(f"Bill amount: {bill}")

            return bill
        
        except ValueError as ex:
            print(tcc.GET_NUMBER_WARNING.format(tcc.BILL_AMOUNT))
            logger.warning(f'{tcc.GET_NUMBER_WARNING.format(tcc.BILL_AMOUNT)} \n {ex}')


def get_input(message:str)->int:
    '''
    Get the percentage tip and amount of patron to split bill among from user, and validate to 
    ensure it is a valid numeric int entry.

    Args:
            message (str): The text to display when asking user for input.

    Returns:
            int: The validated tip percentage or patron count. 
    '''
    logger.info("Getting tip percentage or patron count.")

    if not isinstance(message, str):
        raise(f"Invalid Input: Expected Type 'str' for message '{message}' parameter.")

    while True:
        try:
            user_input = int(input(message))
            return user_input
        
        except ValueError as ex:
            print(tcc.GET_NUMBER_WARNING.format(tcc.TIP_PATRON))
            logger.warning(f'{tcc.GET_NUMBER_WARNING.format(tcc.TIP_PATRON)} \n {ex}')


def calculate_pay_amounts()->float:
    '''
    Function to calculate and split up, how much each of a number of 
    friends/patron is to pay from a bill.

    Returns:

        float: Amount payable by each patron.
    '''   
    logger.info("Calculating payable amounts.")
    
    bill = get_bill_amount("What was the total bill? $")

    tip = get_input("What percentage tip would you like to give? 10, 12, or 15? ")
    logger.info(f"Tip: {tip}")

    people = get_input("How many people to split the bill? ")
    logger.info(f"People: {people}")

    # bill total plus added tip percentage
    grand_total = bill + (bill * (tip/100))
    logger.info(f"Grand Total: {grand_total}")

    split_amount = round((grand_total / people), 2)

    return split_amount


def main()->None:
    """ Main function to start the Tip Calculator Program. """
    try:
        print("Welcome to the tip calculator!")

        logger.info("Starting the Tip Calculator Program.")
        split_amount = calculate_pay_amounts()

        print(tcc.RESULT_MESSAGE.format(split_amount))
        logger.info(tcc.RESULT_MESSAGE.format(split_amount))

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except Exception:
        logger.exception("Error occurred in main Tip Calculator function.")


if __name__ == "__main__":
    main()