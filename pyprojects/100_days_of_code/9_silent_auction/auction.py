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
    bid()
    print(BIDS)


def bid():
    '''
        function to retrieve user bids and store bid in global
        BIDS dictionary.
    '''
    try:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        print('\n' * 50)

        BIDS[name] = bid

    except Exception:
        print("Errror occured retrieving user bid.")


if __name__ == "__main__":
    main()