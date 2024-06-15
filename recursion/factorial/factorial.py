"""
    Python factorial implementation for positive 
    whole numbers.
    @datetime:: September 23, 2023 1:19 am (UTC-5)
    @author:: jac0der
"""


def main():
    # getting number from user - retrieved as a string from user.
    str_number = input("Enter number: ")

    # call to valudate the input to ensure its a number
    validateInput(str_number)


def factorial(number):
    """
        Function to find the factorial of a number
        @input:: number to retrieve factorial for
        @output:: factorial of input number
    """

    # 1! is 1 so return 1 - base case met
    if number == 1 or number == 0:
        return 1

    # recursively call factorial on n - 1
    return number * factorial(number - 1)


def validateInput(value):
    """
        Function to ensure user input is a valid integer
        @input:: number to validate and get factorial for
        @output:: message with factorial result for input number.
    """
    try:
        # try cast input to integer
        number = int(value)

        if number >= 0:

            # at this point user input was successfully cast
            print(f"Factorial of {number} is:", factorial(number))  
            print()
        else:
            print("Only Positive Numbers Valid.") 
            print()       

    except ValueError:
        print("Invalid Input...")
        print()       


if __name__ == "__main__":
    main()
