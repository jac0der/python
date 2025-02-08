"""
    Implementation of the Rock, Paper, Scissors game.
    Rock beats scissors, scissors beat paper, and paper beats rock.
    user decide best of N rounds.

    @datetime:: March 14, 2024 11:57 PM
    @author:: jacoder
"""
import random


# declare global variables
# store computer choices as a tuple - immutable (unchangable throughtout game)
COMPUTER_CHOICE = ('r', 'p', 's')

# track winner of each round, thus winner of game
WINNER = {
    'user': 0,
    'computer': 0
}


def main():
    print("Ready! Set! Shhot! -> Rock!, Paper!, Sissors!")
    print("Start by entering the number of rounds to play.")

    rounds = get_rounds()
    play(rounds)


def get_rounds():
    '''
        Function to get the user's input for the number 
        of rounds of rock paper sissors to play. 
        User's input is also validated to prevent errors.

        @input::  none
        @output::int -> user's entered number of rounds to play
    '''

    # loop as long as an invalid input is entered by user.
    while(True):

        try:
            # try casts users input to integer
            rounds = int(input("Number of rounds: "))

            # only accepts positive whole numbers
            if rounds > 0:
                return rounds
            else:
                print("Invalid Input, Please enter a positive number.")

        except ValueError:
            print("Invalid Input, Please enter a numberic value.")


def get_user_choice():
    ''' 
        function to accept users input of either rock (r),
        paper (p) or scissors (s).

        @input::  none
        @output:: user's chose.
    '''
    running = True

    while running:
         # get user's choice
        print("Enter [r/R - Rock | p/P - Paper | s/S - Sissors]")
        user_choice = input("Your choice: ")

        if user_choice.strip().lower() in COMPUTER_CHOICE:
            return user_choice.strip().lower()


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


def play(rounds):
    '''
        Function to start the rock paper sissors game for number
        of rounds specified as input.

        @input::int -> number of rounds to play.  
        @output::  winner of game.
    '''
    print()

    for i in range(rounds):

        # get user's choice
        user_choice = get_user_choice()

        # get the computer choice randomly
        computer_choice = random.choice(COMPUTER_CHOICE)
        print("Computer's choice is: ", computer_choice)

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


if __name__ == '__main__':
    main()
