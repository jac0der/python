'''
    Create the hangman program.

    @datetime:: October 13, 2024 10:19 am (UTC-5)
    @author:: jacoder
'''
import random as r

stages = ['''
+---+
  |   |
  0   |
 /|\\  |
 / \\  |
      |
========
''', '''
+---+
  |   |
  0   |
 /|\\  |
 /    |
      |
========
''','''
+---+
  |   |
  0   |
 /|\\  |
      |
      |
========
''','''
+---+
  |   |
  0   |
 /|   |
      |
      |
========
''','''
+---+
  |   |
  0   |
  |   |
      |
      |
========
''','''
+---+
  |   |
  0   |
      |
      |
      |
========
''','''
+---+
  |   |
      |
      |
      |
      |
========
'''
]

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
    lives = 6

    # Randomly choose a word from the WORD_LIST and assign it to a variable
    # called chosen_word. Then print it.
    chosen_word = r.choice(WORD_LIST)
    print(chosen_word)

    # Create a "placeholder" with the same number of blanks as the chosen word
    placeholder = ""
    for position in range(len(chosen_word)):
        placeholder += "_"

    print(placeholder)

    game_over = False
    correct_letters = []

    # Use a while loop to let the user guess again.
    while not game_over:
            
        # Ask the user to guess a letter and assign their answer to a variable 
        # called guess. Make guess lowercase.
        guess = input("Guess a letter:  ").lower().strip()

        # Create a "display" that puts the guess letter in the right position and blank (_) in rest of string
        display = ""

        # Change the for loop so that you keep the previous correct guess in previous string
        # Check if the letter the user guessed (guess) is one of the letters in the 
        # chosen_word. Print "Right" if it is, "Wrong" if it's not.
        for letter in chosen_word:

            if letter == guess:
                display += letter
                correct_letters.append(guess)

            elif letter in correct_letters:
                display += letter

            else:
                display += "_"

        print(display)

        if guess not in chosen_word:
            lives -= 1

            if lives == 0:
                game_over = True
                print("You Lose.")

        if "_" not in display:
            game_over = True
            print("You win.")

        print(stages[lives])

    
if __name__ == "__main__":
    main()