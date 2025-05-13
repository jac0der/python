'''
    Program to play a simple rock, paper scissors 
    game, printing ascii art of each option chosen.

    @datetime:: September 26, 2024 8:29 am (UTC-5)
    @author:: jacoder
'''
import sys
import random as r
from art import RPS_ASCII
from logging_custom import jaclog

logger = jaclog.configure('rock_paper_scissors', './rock_paper_scissors.log')


game_params:dict[int,str] = {
    0: 'rock',
    1: 'paper',
    2: 'scissors'
}


def play()->None:
    '''
        Function to start playing the rock, paper, scissors game.
        Prints winner of the game and ascii art of winning option.
    '''
    logger.info("Starting play function.")

    # get user's choice
    player_choice:int = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").rstrip())
    logger.info(f"Player choice: {game_params.get(player_choice)}")

    # exit program if invalid number is entered.
    if player_choice != 0 and player_choice != 1 and player_choice != 2:
        logger.warning("Invalid entry entered. You Lose.")
        exit_program("Invalid entry entered. You Lose.", 0)

    # get computer choice
    computer_choice:int = r.randint(0, 2)
    logger.info(f"Computer choice: {game_params.get(computer_choice)}")

    print(RPS_ASCII[player_choice], end="\n\n")
    print("Computer chose:")
    print(RPS_ASCII[computer_choice])

    winner:int = determine_winner(player_choice, computer_choice)

    if winner == 0:
        print("It's a draw")
        logger.info("It's a draw")
    
    elif winner == 1:
        print("You win!")
        logger.info("You win!")
    
    else:
        print("You lose")
        logger.info("You lose")

    print()


def determine_winner(player_choice:int, computer_choice:int)->int:
    '''
    Function to determine the winner of the rock paper scissors game
    by comparing the user choice with the computer.

    Args:
            player_choice (int): the option selected by user.
            computer_choice (int): the option randomly selected for computer.

    Returns:
            int: integer value indicating who won the game.
                        -1 if computer wins.
                        0 for a draw game
                        1 if the player wins. 
    '''
    logger.info("Determining winner of game.")

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


def exit_program(message:str, code:int=0)->None:
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, >=1 for errors).
    '''
    logger.info(message)
    print(message)
    sys.exit(code)


def main()->None:
    """ Main function to start the Rock Paper Scissors Game.  """
    try:
        logger.info("Starting the Rock Paper Scissors Game.")
        play()

    except ValueError as ex:
        print("Invalid entry. Only Numeric values allowed. You lose.")
        logger.exception(f"Invalid entry. Only Numeric values allowed. You lose.")

    except Exception as ex:
        logger.exception(f"Error occurred in main Rock Paper Scissors function.")


if __name__ == "__main__":
    main()