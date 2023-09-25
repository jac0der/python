"""
    Python factorial implementation for positive 
    whole numbers.
    @datetime:: September 23, 2023 1:19 am (UTC-5)
    @author:: jac0der
"""

# getting number from user - retrieved as a string from user.
str_number = input("Enter number: ")

"""
    Function to find the factorial of a number
    @input:: number to retrieve factorial for
    @output:: factorial of input number
"""
def factorial(number):

    # 1! is 1 so return 1 - base case met
    if number == 1:
        return number

    # recursively call factorial on n - 1
    return number * factorial(number - 1)

"""
    Function to ensure user input is a valid integer
    @input:: number to validate and get factorial for
    @output:: message with factorial result for input number.
"""
def validateInput(value):

    try:
        # try cast input to integer
        number = int(value)

        # at this point user input was successfully cast
        print(f"Factorial of {number} is:", factorial(number))          

    except ValueError:
        print("Invalid Input...")       

# call to valudate the input to ensure its a number
validateInput(str_number)