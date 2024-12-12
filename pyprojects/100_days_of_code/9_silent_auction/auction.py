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
        function to retrieve user bids and store bid in
        dictionary of bid prices.

        @input:: none
        @output:: dict-> bids: dictionary holding all the 
                         entered bid prices.
    '''
    continue_bidding = True
    bids = dict()

    try:

        while continue_bidding:
            name = input("What is your name?: ")
            bid = int(input("What is your bid?: $"))

            if len(name) == 0:
                print('Name is required.', end='\n\n')
                continue

            if bid <= 0:
                print('Bid must be greater than 0.', end='\n\n')
                continue

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
        function to find the highest bidder from the
        dictionary of bidders and their respective bid
        prices.

        @input:: dict->bidder_dictionary: dictionary holding all
                                the entered bid prices.
        @output:: none
    '''
    max_bid = 0
    winner = ''
    
    for bidder, bid_price in bidder_dictionary.items():
        if bid_price > max_bid:
            max_bid = bid_price
            winner = bidder

    '''
        Another short way of retrieving the maximun item from a dictionary
        
    winner = max(bidder_dictionary, key=bidder_dictionary.get)
    max_bid = bidder_dictionary[winner]
    '''

    print(f"The winner is {winner} with a bid of ${max_bid}.")


if __name__ == "__main__":
    main()