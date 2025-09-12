'''
    Silent Auction Program

    This program allows bidders to place bids on an item silently.
    The highest bidder is declared as the winner at the end of the auction.

    @datetime:: December 10, 2024 11:01 pm (UTC-5)
    @author:: jacoder
'''
import art, os, sys, bidding_error
from logging_custom import jaclog

logger = jaclog.configure('silent_auction_100days', './auction.log')


def bid()->dict:
    '''
        Retrieve user bids and store them in a dictionary.

        Returns:
            dict: A dictionary containing bidders' names as keys and their bids as values.
                  Returns None if an error occurs.
    '''
    logger.info('Getting bids from bidders.') 
    is_bidding_active:bool = True
    bids:dict = dict()

    try: 
        float(input("What is your bid?: $"))
        while is_bidding_active:
            name:str = input("What is your name?: ")
            if len(name) == 0:
                logger.warning("Name is required for the bidding process.")
                continue

            try:
                bid_amount:float = float(input("What is your bid?: $"))
                if bid_amount <= 0:
                    logger.warning(f"Bid value for {name} must be greater than 0.")
                    continue
            except ValueError:
                logger.exception(f'Invalid bid entered for {name}.' + '\n' + 'Please enter a valid numeric value.')
                continue

            logger.info(f'{name} has placed a bid of {bid_amount}.')
            bids[name] = bid_amount

            has_more_bidders:str = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()

            if has_more_bidders == "no":
                logger.info('Biding has ended.')
                is_bidding_active = False                
       
            else:
                os.system('cls||clear')  # Clear screen

        return bids

    except Exception as e:
        logger.exception('Errror occured retrieving bidders and their bid prices.')
        raise bidding_error.BiddingError("An error occurred during the bidding process.") from e


def find_highest_bidder(bidder_dictionary:dict)->None:
    '''
        Find the highest bidder from the dictionary of bids.

        Args:
            bidder_dictionary (dict): A dictionary containing bidders' names and their bids.
    '''
    try:
        logger.info('Finding the highest bidder from list of bidders.')
        max_bid:int = 0
        winner:str = ''

        # checking if bidder_dictionary is empty
        if not bidder_dictionary:
            logger.warning("No bids recorded.")
            return
        
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

    except Exception:
        logger.exception('Error occured determining the highest bidder.')
    

def main()->None:
    ''' 
    Main function to run the silent auction program.
    '''
    try:
        logger.info('Started silent auction program.')
        print(art.logo)
        print("Welcome to the secret auction program.")

        bids:dict = bid()  # This may raise a BiddingError
        logger.info(f'Bids: {bids}.')
        find_highest_bidder(bids)
        
    except bidding_error.BiddingError as e:
        logger.error(f'Bidding error: {e}')
        sys.exit(f"Error: {e}. Please check the logs for details.")

    except Exception:
        logger.exception('Error occured in main auction function.')
        sys.exit("An error occurred. Please check the logs for details.")


if __name__ == "__main__":
    main()