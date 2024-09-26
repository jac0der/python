'''
    Program to play a simple rock, paper scissors 
    game, printing ascii art of each option chosen.

    @datetime:: September 26, 2024 8:29 am (UTC-5)
    @author:: jacoder
'''


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
    '''
    try:
        
        user_coice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").rstrip())

    except ValueError:
        print("Invalid entry. Only Numeric values allowed.")


if __name__ == "__main__":
    main()