"""
    Implementation of the Rock, Paper, Scissors game.
    Rock beats scissors, scissors beat paper, and paper beats rock.
    user decide best of N rounds.

    @datetime:: March 14, 2024 11:57 PM
    @author:: jacoder
"""
import random
import os 
import sys
import rps_error

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('rps', './rps.log')

# declare global variables
# store computer choices as a tuple - immutable (unchangable throughtout game)
COMPUTER_CHOICE = ('r', 'p', 's')

# track winner of each round, thus winner of game
WINNER = {
    'user': 0,
    'computer': 0
}


def get_rounds():
    '''
    Get number of rounds from user to play rock paper sissors game. 

    Returns:
            int: The user's entered number of rounds to play.
    '''
    # loop as long as an invalid input is entered by user.
    while True:

        try:
            # try casts users input to integer
            rounds = int(input("Number of rounds: "))

            # only accepts positive whole numbers
            if rounds > 0:
                return rounds
            else:
                print("Invalid Input, Please enter a positive number.")
                logger.warning("Invalid Input, Please enter a positive number.")

        except ValueError:
            print("Invalid Input: Please enter a numberic value.")
            logger.warning("Invalid Input: Please enter a numberic value.")


def play(rounds):
    '''
    Start play the rock paper sissors game.

    Args:
            rounds (int): Number of rounds to play.
    '''
    logger.info('Start playing rounds.')

    if not isinstance(rounds, int):
        raise ValueError(f'Invalid type for rounds. Expected an integer.')

    if rounds < 0:
        raise rps_error.InvalidRoundsError(f'Invalid rounds entered. Expecting a positive number.')

    print()

    for i in range(rounds):

        # get user's choice
        user_choice = get_user_choice()
        logger.info(f"User's choice is {user_choice}")

        # get the computer choice randomly
        computer_choice = random.choice(COMPUTER_CHOICE)
        print("Computer's choice is: ", computer_choice)
        logger.info(f"Computer's choice is {computer_choice}")

        # determine winner
        who_wins_round(user_choice, computer_choice)
    
    # determine who won game
    winner = who_wins_game()

    if winner == 1:
        print(f"After {rounds} rounds, User wins the game!")
    elif winner == -1:
        print(f"After {rounds} rounds, Computer wins the game!")
    else:
        print("No winner - tie game!")


def get_user_choice():
    ''' 
    Get users' input of either rock (r), paper (p) or scissors (s).
    Returns:
            str: The user's choice.
    '''
    logger.info('Getting user selection.')
    while True:
         # get user's choice
        print("Enter [r/R - Rock | p/P - Paper | s/S - Sissors]")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice in COMPUTER_CHOICE:            
            return user_choice

        logger.warning(f'Invalid selection: User entered {user_choice} instead of either r/p/s.')
            

# Rock beats scissors, scissors beat paper, and paper beats rock.
def who_wins_round(user_choice, computer_choice):
    '''
        function to determine winner of round based on 
        user and computer inputs.

        @input::int user_choice 
                    the user's entered choice
        @input:: int computer_choice
                     the randomly selected compouter choice.
        @output::str
                  message indicating who wins round, otherwise, print tie.              
    '''

    if user_choice == computer_choice:
        print("Round Tie!")
        print()

    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "s" and computer_choice == "p") or \
         (user_choice == "p" and computer_choice == "r"):

         # update user's round count
         WINNER['user'] += 1
         
         print("User wins round!")
         print()
         
    else:
        # update computer's round count
         WINNER['computer'] += 1
         
         print("Computer wins round!")
         print()


def who_wins_game():
    '''
        Function to determine which player won the most rounds,
        hence won the game, otherwise, a tie.

        @input:: none
        @output::str -> the player who won the game or string tie.
    '''

    if WINNER['user'] > WINNER['computer']:
        return 1 # user wins
    elif WINNER['computer'] > WINNER['user']:
        return -1 # computer wins
    else:
        return 0 # tie


def exit_program(message, code=0):
    '''
    Centralized exit function to handle program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)


def main():
    try:
        logger.info('Starting Rock, Paper, Scissors Game...')
        print("Ready! Set! Shhot! -> Rock!, Paper!, Sissors!")
        print("Start by entering the number of rounds to play.")   

        rounds = get_rounds()
        play(rounds) 

    except ValueError as ex:
        logger.warning('Invalid input to get_rounds(rounds) function.')

    except KeyboardInterrupt as ex:
        exit_program('\nUser exited program...')

    except Exception as ex:
        logger.exception("Error occured in main calculator function.")
        exit_program('An error occured. Please check the logs for details.')


if __name__ == '__main__':
    main()
