'''
    Program to guide a user to find a treasure on an island,
    using conditional logic.

    @datetime:: September 19, 2024 2:14 am (UTC-5)
    @author:: jacoder
'''


def main():
    draw_greet_banner()
    find_treasure()



def draw_greet_banner():
    '''
        Function to display the welcome treasure banner for
        program

        @input: none
        @output: str -> a treasure box display as a greeter to program.
    '''
    print("*******************************************************************************")
    print("          |                   |                  |                     |      |")
    print(" _________|________________.=""_;=.______________|_____________________|_______")
    print("Welcome to Treasure Island.")


def find_treasure():
    print("You're at a Cross road. Where do you want to go?")
    direction = input('     Type "left" or "right"\n')
    


if __name__ == "__main__":
    main()
