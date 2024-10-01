'''
    Create a password generator program.

    @datetime:: October 1, 2024 3:00 am (UTC-5)
    @author:: jacoder
'''
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    print("Welcome to the Jacoder Password Generator!")

    # ensures that user enters a valid integer whole number
    while True:

        try:

            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input(f"How many symbols would you like?\n"))
            nr_numbers = int(input(f"How many numbers would you like?\n"))

            if nr_letters >= 0 and nr_symbols >= 0 and nr_numbers >= 0:
                break
            else:
                print("Enter only positive whole numbers.\n")

        except ValueError:
            print("Invalid entry, please try again\n")

    print()
    sequence_pwd = generate_sequential_pwd(nr_letters, nr_symbols, nr_numbers)
    random_pwd = generate_random_pwd(nr_letters, nr_symbols, nr_numbers)

    print(f'sequential password is: {sequence_pwd}', end='\n')
    print(f'randomized random password is: {random_pwd}', end='\n\n')


def generate_sequential_pwd(nr_letters, nr_symbols, nr_numbers):
    '''
        Function to generate a random password comprised of letters and/or
        symbols and/or numbers, in that specific order, after each letters,
        symbols or numbers have been randomly slected.
        Eazy Level - Order not randomised: e.g. 4 letter, 2 symbol, 2 number = JduE&!91

        @input: int -> nr_letters: number of letters to be randomly selected
                                   for the password.
                int -> nr_symbols: int:: number of symbols to be randomly selected
                                   for the password.
                int -> nr_numbers: int:: number of numbers to be randomly selected
                                   for the password.

        @output:: str -> password: the randomly generated password.
    '''
    password = ''

    # looping the letters list to pull out nr_letters amount of letters.
    for number in range(0, nr_letters):
        password += random.choice(letters)

    # looping the symbols list to pull out nr_symbols amount of letters.
    for number in range(0, nr_symbols):
        password += random.choice(symbols)

    # looping the numbers list to pull out nr_numbers amount of numbers.
    for number in range(0, nr_numbers):
        password += random.choice(numbers)

    return password


def generate_random_pwd(nr_letters, nr_symbols, nr_numbers):
    '''
        Function to generate a random password comprised of letters and/or
        symbols and/or numbers, in a random order.
        Hard Level - Order of characters randomised: e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

        @input: int -> nr_letters: number of letters to be randomly selected
                                   for the password.
                int -> nr_symbols: int:: number of symbols to be randomly selected
                                   for the password.
                int -> nr_numbers: int:: number of numbers to be randomly selected
                                   for the password.

        @output:: str -> password: the randomly generated password.
    '''
    # create an empty list to put randome selctions in.
    selection = list()
    password = ''

    # first set up the selection list with randomly selected letters.
    for number in range(0, nr_letters):
        letter = random.choice(letters)
        selection.append(letter)

    # select random symbols and insert at a random spot in selection list
    for number in range(0, nr_symbols):
        index = random.randint(0, len(selection))
        selection.insert(index, random.choice(symbols))

    # select random numbers and insert at a random spot in selection list
    for number in range(0, nr_numbers):
        index = random.randint(0, len(selection))
        selection.insert(index, random.choice(numbers))

    # formulating the final random password string
    for item in selection:
        password = password + item

    return password


if __name__ == "__main__":
    main()