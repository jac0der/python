'''
    Create a simple program to generate the possible name of
    a band based on user inputs to questions.

    @datetime:: September 17, 2024 9:00 am (UTC-5)
    @author:: jacoder
'''
import sys

EXIT_MESSAGE:str = 'Goodbye!'

def exit_program(message:str, code:int=0)->None:
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    print(message)
    sys.exit(code)


def generate_band_name()->str:
    '''
        Function to accept two user inputs then concatenate
        inputs to form possible name of band.
        @input:: none
        @output:: str - name of band
    '''
    try:
        print('Welcome to the Band Name Generator.')

        city = input("What's the name of the city you grew up in?\n")
        pet = input("What's your pets's name?\n")

        band_name = f"Your band name could be {city + ' ' + pet}"
        return band_name
    
    except (KeyboardInterrupt, EOFError):
        exit_program("\n"+EXIT_MESSAGE)


def main()->None:
    """ Main function to start the Band Generator program. """
    print(generate_band_name())


if __name__ == "__main__":
    main()