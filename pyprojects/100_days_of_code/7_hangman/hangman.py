'''
    Create the hangman program.

    @datetime:: October 13, 2024 10:19 am (UTC-5)
    @author:: jacoder
'''


WORD_LIST = [
    "aardvark", "baboon", "camel"
]


def main():
    generate_random_word()


def generate_random_word():
    '''
        Function to generate a random word from WORD_LIST
        for user to guess.
    '''

    # Randomly choose a word from the WORD_LIST and assign it to a variable
    # called chosen_word. Then print it.

    # Ask the user to guess a letter and assign their answer to a variable 
    # called guess. Make guess lowercase.

    # Check if the letter the user guessed (guess) is one of the letters in the 
    # chosen_word. Print "Right" if it is, "Wrong" if it's not.
    pass


if __name__ == "__main__":
    main()