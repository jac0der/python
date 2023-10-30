import re


card_length = 0

"""
    Constants for starting digits
    Use tuple for starting digits for master card and american express cards
    because Tuples are immutable, cannot change.
"""
MASTER_CARD_START_DIGITS = ('51', '52', '53', '54', '55')
AMERICAN_EXPRESS_START_DIGITS = ('34', '37')
VISA_START_DIGIT = ('4',)


"""
    Function to get input credit card number from user.
    Regular exppression is used to ensure user enters string
    with only digits, otherwise INVALID is returned.
    The length of the input string is also validated to be
    either 13, 15 or 16, otherwise INVALID is returned.
"""


def getCardInput():
    global card_length
    number_pattern = "^\\d+$"

    # get input card number from user
    credit_card_number = input("Number: ")
    card_length = len(credit_card_number)

    # Returns Match object using regex
    isDigits = re.match(number_pattern, credit_card_number)

    if isDigits and (card_length == 15 or card_length == 16 or card_length == 13):
        return validateCard(credit_card_number)
    else:
        return "INVALID"


"""
    Function to validate type of credit card, and if it
    is actually a valid credit card.
    @input:: card_number:: credit card number entered by user
    @output:: The type of credit card, American Express, Master Card, Visa or INVALID
"""


def validateCard(card_number):
    # access global variable within scope of this function
    global card_length

    card_status = "INVALID"

    # turn input card number into a list (of strings)
    digits = list(card_number)

    first_2_digits = digits[0] + digits[1]
    first_digit = digits[0]

    # check if card is American Express
    if card_length == 15 and first_2_digits in AMERICAN_EXPRESS_START_DIGITS:
        card_status = "AMEX"

    # check if card is Master Card
    elif card_length == 16 and first_2_digits in MASTER_CARD_START_DIGITS:
        card_status = "MASTERCARD"

    # check if card is VISA Card
    elif card_length in [13, 16] and first_digit in VISA_START_DIGIT:
        card_status = "VISA"

    # is card validt still at this point, based on length of card number entered.
    if card_status != "INVALID":
        if calculateCheckSum(digits):
            return card_status
        else:
            card_status = "INVALID"
            return card_status
    else:
        return card_status


"""
    Function to start the process of validating the credit card.
    Function checks the length of the card numbers to see if its an
    even or odd amount of numbers that makes up the credit card number.
    This is done to be able to use List Comprehension in the performLuhn
    function with a step of 2, so knowing the length of the card
    digit will determine which index to start.

    @input::card_digits:: List of card digits entered by user
    @output:: Boolean, True if card is valid, otherwise False.
"""


def calculateCheckSum(card_digits):
    global card_length

    # length of card digits is even
    if card_length % 2 == 0:
        if performLuhn(card_digits, 0, 1):
            return True
        else:
            return False

    # length of card digits is odd
    else:
        if performLuhn(card_digits, 1, 0):
            return True
        else:
            return False


"""
    Function to perform the Luhn algorithm on the card number to
    determine if is valid credit card.
    @inputs::
        digits:: List of card digits entered by user
        products_index::  index in the digits list to start multiplying
                          digits by 2.
        unmultiplied_sum_index:: index in the digits list to start addition
                                 of digits that are not multiplied by 2.
    @output:: Boolean, True if card is valid, otherwise False.
"""


def performLuhn(digits, products_index, unmultiplied_sum_index):
    luhn_total = 0
    unmultiplied_sum = 0
    alternate_digits_sum = 0

    """
      list comprehension to get products of alternate card number digits, cast
      each string digit to integer before multiplying.
      Then cast back the product result to string.
      start at products_index, go to end of List, at a step of 2 digits
    """
    alternate_products = [str(int(value) * 2) for value in digits[products_index::2]]

    # set up 2 for loops to loop through each digit of the product result values
    for product in alternate_products:
        for digit in product:
            alternate_digits_sum += int(digit)

    # summing alternate digits which were not apart of the multiplication by 2
    for digit in digits[unmultiplied_sum_index::2]:
        unmultiplied_sum += int(digit)

    # total luhun
    luhn_total = alternate_digits_sum + unmultiplied_sum

    # check if total last digit is 0, by using the modulo operator
    if luhn_total % 10 == 0:
        return True  # card is a valid card
    else:
        return False  # card is NOT a valid card


print(getCardInput())
