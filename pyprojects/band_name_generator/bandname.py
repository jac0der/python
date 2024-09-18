'''
    Create a simple program to generate the possible name of
    a band based on user inputs to questions.

    @datetime:: September 17, 2024 9:00 am (UTC-5)
    @author:: jacoder
'''


def main():
    generate_band_name()


def generate_band_name():
    '''
        Function to accept two user inputs then concatenate
        inputs to form possible name of band.
        @input:: none
        @output:: str - name of band
    '''
    print('Welcome to the Band Name Generator.')

    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pets's name?\n")

    print(f"Your band name could be {city + ' ' + pet}")


if __name__ == "__main__":
    main()