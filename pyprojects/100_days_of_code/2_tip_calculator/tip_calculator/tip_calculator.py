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
            return bill
        
        except ValueError as ex:
            print(tcc.GET_NUMBER_WARNING.format('bill'))
            logger.warning(f'{tcc.GET_NUMBER_WARNING.format('bill')} \n {ex}')


def calculate_pay_amounts()->float:
    '''
    Function to calculate and split up how much each of a number of 
    friends/patron is to pay from a bill.

    Returns:

        float: Amount payable by each patron.
    '''
   
    logger.info("Calculating payable amounts.")
    print("Welcome to the tip calculator!")
    
    bill = get_bill_amount("What was the total bill? $")

    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))

    # bill total plus added tip percentage
    grand_total = bill + (bill * (tip/100))

    split_amount = round(grand_total / people, 2)

    
        # print(f"Each person should pay: ${split_amount}")


    return split_amount


def main()->None:
    """ Main function to start the Tip Calculator Program. """
    try:
        logger.info("Starting the Tip Calculator Program.")
        pay_amount = calculate_pay_amounts()
        print(f"Each person should pay: ${pay_amount}")

    except Exception:
        logger.exception("Error occurred in main Tip Calculator function.")


if __name__ == "__main__":
    main()