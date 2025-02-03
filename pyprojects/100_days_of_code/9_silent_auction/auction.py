'''
    Create a silent auction program, allowing
    bidders to bid once for an item.

    @datetime:: December 10, 2024 11:01 pm (UTC-5)
    @author:: jacoder
'''
import art, os, sys

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../logging')))
import jaclog
logger = jaclog.configure('silent_auction_100days', './auction.log')


def bid():
    '''
        function to retrieve user bids and store bid in
        dictionary of bid prices.

        Args:
                none
        Returns:
                dict(): bids dictionary holding all the entered bid prices and bidders.
    '''
    logger.info('Getting bids from bidders.') 
    continue_bidding = True
    bids = dict()

    try: 
        while continue_bidding:
            name = input("What is your name?: ")
            if len(name) == 0:
                logger.warning("Name is required for the bidding process.")
                continue

            try:
                bid = float(input("What is your bid?: $"))
                if bid <= 0:
                    logger.warning(f"Bid value for {name} must be greater than 0.")
                    continue
            except ValueError:
                logger.exception(f'Invalid bid entered for {name}.' + '\n' + 'Please enter a valid numeric value.')
                continue

            logger.info(f'{name} has placed a bid of {bid}.')
            bids[name] = bid

            morebids = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()

            if morebids == "no":
                logger.info('Biding has ended.')
                continue_bidding = False                
       
            elif morebids == "yes":
                logger.info('Continue bidding - there are more bidders.')
                os.system('cls||clear')  # Clear screen

        return bids

    except Exception:
        logger.exception('Errror occured retrieving bidders and their bid prices.')
        return None


def find_highest_bidder(bidder_dictionary):
    '''
        function to find the highest bidder from the
        dictionary of bidders and their respective bid
        prices.

        Args:
                bidder_dictionary (dict()): dictionary holding all the entered bid prices.
        Returns:
                none
    '''
    logger.info('Finding the highest bidder from list of bidders.')
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
    logger.info(f'The winner is {winner} with a bid of ${max_bid}.')


def main():
    try:
        logger.info('Started silent auction program.')
        print(art.logo)
        print("Welcome to the secret auction program.")
        
        bids = bid()

        if bids is not None:
            logger.info(f'Bids: {bids}.')
            find_highest_bidder(bids)
        else:
            logger.warning('No bids recorded. Error geting bidders with bid prices.')

    except Exception:
        logger.exception('Error occured in main auction function.')
        sys.exit(1)


if __name__ == "__main__":
    main()