'''
    Create a password generator program.

    @datetime:: October 1, 2024 3:00 am (UTC-5)
    @author:: jacoder
'''
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def main():
    print("Welcome to the Jacoder Password Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    sequence_pwd = generate_sequential_pwd(nr_letters, nr_symbols, nr_numbers)
    random_pwd = generate_random_pwd(nr_letters, nr_symbols, nr_numbers)

    print(sequence_pwd)


def generate_sequential_pwd(nr_letters, nr_symbols, nr_numbers):
    '''
    '''
    # create an empty list to put randome selctions in.
    selection = list()

    # looping the letters list to pull out nr_letters amount of letters.
    for number in range(0, nr_letters):
        letter = random.choice(letters)
        selection.append(letter)

    # looping the symbols list to pull out nr_symbols amount of letters.
    for number in range(0, nr_symbols):
        symbol = random.choice(nr_symbols)
        selection.append(symbol)

    return selection


def generate_random_pwd(nr_letters, nr_symbols, nr_numbers):
    '''
    '''
    pass


if __name__ == "__main__":
    main()