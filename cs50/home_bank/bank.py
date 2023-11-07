"""
    Program to prompt the user for a greeting. 
    If the greeting starts with “hello”, output $0 . 
    If the greeting starts with an “h” (but not “hello”), output $20. 
    Otherwise, output $100 . Ignore any leading whitespace in the user’s greeting, 
    and treat the user’s greeting case-insensitively.

    @datetime:: November 6, 2023 10:25 pm (UTC-5)
    @author:: jac0der
"""


def main():
    # get input from user and ignore case by lowering all charaters,
    # then removing any leading or trailing spaces.
    greeting = input('Geeting: ').lower().strip()

    try:
        if greeting.startswith('hello'):
            print('$0')
        elif greeting[0] == 'h' and not(greeting.startswith('hello')):
            print('$20')
        else:
            print('$100')

    except IndexError:
        print('Error - Invalid input.')


if __name__ == '__main__':
    main()
