"""
    Rock beats scissors, scissors beat paper, and paper beats rock.
    Agree ahead of time whether you’ll count off “rock, paper, scissors, shoot” or just 
    “rock, paper, scissors.”
    Use rock, paper, scissors to settle minor decisions or simply play to pass the time.

    user decide best of N tries

    @author::
    @datetime::
"""


def main():
    print("Ready! Set! -> Rock!, Paper!, Sissors!")
    print("Start by entering the number of rounds to play.")

    rounds = get_rounds()


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



# get random computer choice

# determine winner - compare user and computer choice


if __name__ == '__main__':
    main()
