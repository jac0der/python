"""
    Implementation of the FIZZBUZZ program. Find details in the
    FIZZBUZZ_README.
    
    @datetime:: November 05, 2023 10:21 pm (UTC-5)
    @author:: jac0der
"""


# declaring global multiple constant values to check for.
MULT3 = 3
MULT5 = 5


def main():
    fizzbuzz()


def is_multiple(dividend, divisor):
    """
        Function to determine if a divisor is a multiple of dividend.
        Used the modulo (%) operator to determine if divisor is a multiple
        of dividend. Modulo operator returns the remainder from a division,
        if zero (0) is returned, then divisor is a multiple of dividend.
        @inputs::
                dividend - number being divided
                divisor - number being check to see if it is a multiple
                        of dividend.
        @output:: Boolean - True if divisor is a multiple of dividend,
                otherwise, False.
    """
    if (dividend % divisor) == 0:
        return True
    else:
        return False


def fizzbuzz():
    """
        Function to loop through numbers from 1 to 100,
        printing 
            - FizzBuzz if a number is both a multiple of 3 and 5
            - Fizz if a number is a multiple of 3
            - Buzz if a number is a multiple of 5

        The range() method is used to produce the numbers from 1 - 100.
        @input:: none
        @output:: none
    """
    
    # range method goes up to but not including the last index specified, so 
    # why 101 is specified, in dorder to include 100.
    for number in range(1, 101):
        #check if number is both a multiple of 3 AND 5
        if is_multiple(number, 3) and is_multiple(number, 5):
            print('FizzBuzz ', end='')

        # check ifnumber is multiple of 3
        elif is_multiple(number, 3):
            print('Fizz ', end='')

        # check if number is multiple of 5
        elif is_multiple(number, 5):
            print('Buzz ', end='')

        # no multiple found, print number
        else:
            print(number,' ', end='')


# call main() method which calls the fizzbuzz method
if __name__ == "__main__":
    main()