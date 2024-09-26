'''
    Program to play a simple rock, paper scissors 
    game, printing ascii art of each option chosen.

    @datetime:: September 26, 2024 8:29 am (UTC-5)
    @author:: jacoder
'''
import random as r


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


def main():
    play()


def play():
    '''
        Function to start playing the rock, paper, scissors game.
        @input:: none
        @output:: winner of the game, ascii art of winning option.
    '''
    try:
        # get user's choice
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").rstrip())

        # get computer choice
        computer_choice = r.randint(0, 2)

        winner = determine_winner(player_choice, computer_choice)

        if winner == 0:
            print("draw")
        
        elif winner == 1:
            print("You won!")
        
        else:
            print("Computer wins!")

    except ValueError:
        print("Invalid entry. Only Numeric values allowed.")


def determine_winner(player_choice, computer_choice):
    '''
    '''
    if player_choice == computer_choice:
        return 0

    elif ((player_choice == 0 and computer_choice == 2) or 
          (player_choice == 1 and computer_choice == 0) or
          (player_choice == 2 and computer_choice == 1)):
        # player wins
        return 1

    else:
        # computer wins
        return -1


if __name__ == "__main__":
    main()