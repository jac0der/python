'''
    Program to play a simple rock, paper scissors 
    game, printing ascii art of each option chosen.

    @datetime:: September 26, 2024 8:29 am (UTC-5)
    @author:: jacoder
'''
import random as r
from logging_custom import jaclog

logger = jaclog.configure('rock_paper_scissors', './rock_paper_scissors.log')


# define the ascii art list for rock, paper and scissors
RPS_ASCII = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]


def play()->None:
    '''
        Function to start playing the rock, paper, scissors game.
        @input:: none
        @output:: winner of the game, ascii art of winning option.
    '''
    try:
        # get user's choice
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").rstrip())

        # exit program if invalid number is entered.
        if player_choice != 0 and player_choice != 1 and player_choice != 2:
            print("Invalid entry entered. You Lose.")
            return 0

        # get computer choice
        computer_choice = r.randint(0, 2)

        print(RPS_ASCII[player_choice], end="\n\n")
        print("Computer chose:")
        print(RPS_ASCII[computer_choice])

        winner = determine_winner(player_choice, computer_choice)

        if winner == 0:
            print("It's a draw")
        
        elif winner == 1:
            print("You win!")
        
        else:
            print("You lose")

        print()

    except ValueError:
        print("Invalid entry. Only Numeric values allowed. You lose.")


def determine_winner(player_choice, computer_choice):
    '''
        Function to determine the winner of the rockk paper scissors game
        by comparing the user choice with the computer.
        @input:: int -> player_choice: the option selected by user.
                 int -> computer_choice: the option randomly selected for computer.

        @output:: int -> integer value indicating who won the game.
                         -1 if computer wins.
                         0 for a draw game
                         1 if the player wins. 
    '''
    # draw game test
    if player_choice == computer_choice:
        return 0

    # player win test
    elif ((player_choice == 0 and computer_choice == 2) or 
          (player_choice == 1 and computer_choice == 0) or
          (player_choice == 2 and computer_choice == 1)):
        # player wins
        return 1

    # otherwise, computer wins
    else:
        # computer wins
        return -1


def main()->None:
    """ Main function to start the Rock Paper Scissors Game.  """
    try:
        play()

    except Exception as ex:
        logger.exception("Error occurred in main Rock Paper Scissors function.")


if __name__ == "__main__":
    main()