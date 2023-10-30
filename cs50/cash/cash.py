def main():
    getCoinCount(getChangeOwed())


# loop until user enters a valid positive dollar value
def getChangeOwed():
    while True:
        try:
            change = float(input("Change owed: "))
        
        except ValueError:
            continue

        if change > 0:
            return change


"""
    Function to determine the amount of coins needed to produce
    change.
    @input:: dollar value amount for changed owed.
    @output:: total coins needed for change
"""


def getCoinCount(change):
    # 100 cents = $1 and 200 cents = $2 etc...
    cents = convertDollarToCents(change)

    quarters = calculate_quarters(cents)
    cents = int(cents - (quarters * 25))

    dimes = caluculate_dimes(cents)
    cents = int(cents - (dimes * 10))

    nickels = calculate_nickels(cents)
    cents = int(cents - (nickels * 5))

    pennies = calculate_pennies(cents)
    cents = int(cents - (pennies * 1))

    coin_count = int(quarters + dimes + nickels + pennies)

    print(coin_count)


# function to convert from dollar to cents
def convertDollarToCents(change):
    return change * 100


# calculate amount of quarters needed for change
def calculate_quarters(cents):
    return int(cents / 25)


# calculate amount of dimes needed for change
def caluculate_dimes(cents):
    return int(cents / 10)


# calculate amount of nickels needed for change
def calculate_nickels(cents):
    return int(cents / 5)


# calculate amount of pennies needed for change
def calculate_pennies(cents):
    return int(cents / 1)


# call to main function to start execution of program/script.
main()