'''
    Program to calculate amounts payable by a number
    of patrons or friends from a bill, inclusive of
    a percentage tip added to bill total.

    @datetime:: September 18, 2024 5:14 am (UTC-5)
    @author:: jacoder
'''


def main():
    calculate_pay_amounts()


def calculate_pay_amounts():
    '''
        Function to calculate and split up how much each 
        of a number of friends/patron is to pay from a
        bill.

        @input: none
        @output: float -> amount payable by each patron.
    '''
    print("Welcome to the tip calculator!")

    bill_total = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    split = int(input("How many people to split the bill? "))

    # bill total plus added tip
    grand_total = bill_total + (bill_total * (tip/100))
    print(grand_total)

    split_amount = grand_total / split

    print(f"Each person should pay: ${round(split_amount, 2)}")


if __name__ == "__main__":
    main()