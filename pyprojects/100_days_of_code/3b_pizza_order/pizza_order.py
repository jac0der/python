'''
    Create a simple program to automatically calculate the
    bill for a pizza ordered by a client based on a 
    number of options.

    Small pizza (S): $15
    Medium pizza (M): $20
    Large pizza (L): $25

    Add peperoni for small pizza (Y or N): +$2
    Add peperoni for medium or large pizza (Y or N): +$3
    Add extra cheese for any size pizza (Y or N): +$1

    @datetime:: September 20, 2024 5:29 am (UTC-5)
    @author:: jacoder
'''


def main():
    print("Welcome to Python Pizza Deliveries!")
    get_pizza_bill()


def get_pizza_bill():
    '''
        Function to calculate the pizza bill based on 
        options for pizza selected by the client. 
    '''
    bill = 0
    valid_entry = False

    while not valid_entry:
        size = input("What size pizza do you want? S, M, L or q to quit: ").lower()

        # amount to pay based on the pizza size choice.
        if size == 's':
            bill += 15
            valid_entry = True

        elif size == 'm':
            bill += 20
            valid_entry = True

        elif size == 'l':
            bill += 25
            valid_entry = True

        elif size == "q":       # exit program
            print("Bye...")
            return 0

        else:
            print("Invalid pizza size entered. Please try again.\n")

    # reset valid_entry
    valid_entry = False
    while not valid_entry:
        pepperoni = input("Do you want pepperoni on your pizza? Y or N or q to quit: ").lower()

            # how much more to add to bill based on pepperoni choice.
        if pepperoni == "y":

            if size == "s":
                bill += 2
            else:           # add $3 for medium or large pepperoni pizzas
                bill += 3

            valid_entry = True

        elif pepperoni == "q":
            print("Bye...")
            return 1

        elif pepperoni == "n":
            valid_entry = True

        else:
            print("Invalid pepperoni option entered. Please try again.\n")


    valid_entry = False

    while not valid_entry:
        extra_cheese = input("Do you want extra cheese Y or N or q to quit: ").lower()

        # add cost for extra cheese.
        if extra_cheese == "y":
            bill += 1
            valid_entry = True

        elif extra_cheese == "n":
            valid_entry = True
        
        elif extra_cheese == "q":
            print("Bye...")
            return 2
        else:
            print("Invalid extra cheese option entered. Please try again.\n")


    print(f"Your final bill is: ${bill}.")


if __name__ == "__main__":
    main()