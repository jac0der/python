'''
    Create a silent auction program, allowing
    bidders to bid once for an item.

    @datetime:: December 10, 2024 11:01 pm (UTC-5)
    @author:: jacoder
'''
import art


def main():
    print(art.logo)
    print("Welcome to the secret auction program.")
    
    bids = bid()

    # print highest bidder once there were no errors.
    if bids != None:
        find_highest_bidder(bids)


def bid():
    '''
        function to retrieve user bids and store bid in global
        BIDS dictionary.
    '''
    continue_bidding = True
    bids = dict()

    try:

        while continue_bidding:
            name = input("What is your name?: ")
            bid = int(input("What is your bid?: $"))

            if len(name) == 0:
                print('Name is required.')
                return None

            bids[name] = bid

            morebids = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()

            if morebids == "no":
                continue_bidding = False                
       
            elif morebids == "yes":
                print("\n" * 20)

        return bids

    except ValueError:
        print("Invalid bid price entered, only numeric values allowed.")
        return None

    except Exception:
        print("Errror occured retrieving user bids.")
        return None


def find_highest_bidder(bidder_dictionary):
    '''

    '''
    max_bid = 0
    winner = ''

    for bidder, bid_price in bidder_dictionary.items():
        if bid_price > max_bid:
            max_bid = bid_price
            winner = bidder

    print(f"The winner is {winner} with a bid of ${max_bid}.")


if __name__ == "__main__":
    main()