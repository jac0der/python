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
    print('''
                *******************************************************************************
                |                   |                  |                     |
                _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                        |                `"=._o`"=._      _`"=._                     |
                _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/______ /
                *******************************************************************************
    ''')


def find_treasure():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    print("You're at a Cross road. Where do you want to go?")

    while True:
        direction = input('     Type "left" or "right or q to quit"\n').strip().lower()

        if direction == "left":
            
            while True:
                print("You've come to a lake. There is an island in the middle of the lake.")

                boat_or_swim = input('  Type "wait" to wait for a boat. Type "swim" to swim accross, or q to quit\n').strip().lower()

                if boat_or_swim == "wait":
                    
                    while True:
                        print("You arrive at the island unharmed. There is a house with 3 doors.")
                        door_color = input("    One red, one yellow and one blue. Which colour do you choose? or q to quit\n").strip().lower()

                        if door_color == "red":
                            print("It's a room full of fire. Game Over.")
                            return 0

                        elif door_color == "yellow":
                            print("You found the treasure! You Win!")
                            return 0

                        elif door_color == "blue":
                            print("You enter a room of beasts. Game Over.")
                            return 0

                        else:
                            print("Invalid color entered. Please try again.\n")
                    
                elif boat_or_swim == "swim":
                    print("You get attacked by an angry trout. Game Over.")
                    return 0

                else:
                    print("Invalid entry for boat or swim option.\n")

        elif direction == "right":
            print("You fell into a hole. Game Over.")
            break

        else:
            print("Invalid direction enetered. Please try again.\n")
    

if __name__ == "__main__":
    main()
