'''
    Create a silent auction program, allowing
    bidders to bid once for an item.

    @datetime:: December 10, 2024 11:01 pm (UTC-5)
    @author:: jacoder
'''
import art


BIDS = dict()


def main():
    print(art.logo)
    
    Running = True

    while Running:
        bid()
        morebids = input("Are there any other bidders? Type 'yes' or 'no'.\n\t").strip().lower()

        if morebids != "yes":
            Running = False
            
        print("\n" * 10)

    max_bid = 0
    winner = ''

    for name, bidd in BIDS.items():
        if bidd > max_bid:
            max_bid = bidd
            winner = name

    print(f"The winner is {winner} with a bid of ${max_bid}")


def bid():
    '''
        function to retrieve user bids and store bid in global
        BIDS dictionary.
    '''
    try:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))

        BIDS[name] = bid

    except Exception:
        print("Errror occured retrieving user bid.")


if __name__ == "__main__":
    main()