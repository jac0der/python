'''
    Program to guide a player to survive or escape 
    the jungle based on selected options.

    @datetime:: September 21, 2024 5:25 am (UTC-5)
    @author:: jacoder
'''


def main():
    draw_banner()
    survive_jungle()


def draw_banner():
    print('''
        d8b                         888         
        Y8P                         888         
                                    888         
        8888888  88888888b.  .d88b. 888 .d88b.  
        "888888  888888 "88bd88P"88b888d8P  Y8b 
        888888  888888  888888  88888888888888 
        888Y88b 888888  888Y88b 888888Y8b.     
        888 "Y88888888  888 "Y88888888 "Y8888  
        888                     888            
       d88P                Y8b d88P            
    888P"                  "Y88P" 
    ''')


def survive_jungle():
    print("Welcome to Jungle Survival.")
    print("Your mission is to survive by finding an escape route out of the Jungle.")
    print("You are deep in the jungle, at your feet is a waterproof back pack and a few resource items.")
    print("Pack your backpack or leave backpack.")
    print(''' 
                0. Knife
                1. Rope (50 feet)
                2. Scuba Gears (suit, goggles, tank and fin)
                3. Drinking Water
                4. Juice
                5. Large Meat
                6. Flashlight
                7. Boots
                8. Horn
                9. Flare
                10. Compass
                11. Bread
                12. Rifle
                13. Bow and Arrows
                14. Parashoot

    \n''')

    choice = input("Choose only '5' items (1,2,4,5):   ")




if __name__ == "__main__":
    main()