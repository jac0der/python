'''
    Create a black jack game.

    @datetime:: February 12, 2025 8:03 pm (UTC-5)
    @author:: jac0der
'''
import art
import random
import blackjack_enum as bje
import blackjack_constants as bjc
from models.dealer import Dealer
from models.player import Player
from logging_custom import jaclog


logger = jaclog.configure('blackjack', './blackjack.log')

# create dealer and player objects
dealer:Dealer = Dealer()
player:Player = Player()


def get_deal_amount()->int:
    '''
    Get a random number to be used to determine how many more cards
    should be dealt to either player or dealer.

    Returns:
            int: The total amount of cards to deal.
    '''
    logger.info("Getting new deal amount.")
    return random.randint(1, 3)


def deal(deal_amount:int, cards_list:list[int], current_cards:list[int])->list[int]:
    '''
    Update the cards list for either the player or dealer with newly dealt cards.

    Args:
            deal_amount (int): The amount of cards to deal to player or dealer.
            cards_list list[int]: The valid cards to deal from.
            current_cards list[int]: The current cards list for either player or dealer.
    Returns:
            list[int]: The updated cards list for the player or dealer with newly dealt cards.
    '''
    if not isinstance(deal_amount, int):
        raise ValueError('Invalid Type: Expected an integer for deal_amount.')

    if not isinstance(cards_list, list) or not all(isinstance(card, int) for card in cards_list):
        raise TypeError('Invalid Type: cards_list must be a list of integers.')

    if not isinstance(current_cards, list) or not all(isinstance(card, int) for card in current_cards):
        raise TypeError('Invalid Type: current_cards must be a list of integers.')

    logger.info(f"Performing deal for deal amount {deal_amount}.")
    
    new_cards = random.sample(cards_list, deal_amount)  # Pick multiple cards at once
    current_cards.extend(new_cards)  # Add to player's current cards

    return current_cards
    

def display_current_cards_and_totals(player_text:str, dealer_text:str, hide_dealer: bool=True)->None:
    '''
    Displays the current cards for player and dealer along with the card totals.

    Args:
            player_text (str): Text to display showing  players cards. e.g. Your Cards:
            dealer_text (str): Text to display showing dealers cards. e.g. Dealers first cards:
            hide_dealer (bo0l): Disguise dealers card if True, otherwise False, show Dealers card.
    '''
    dealer_score = str(dealer.get_cards_total())
    dealer_cards = dealer.get_cards()
    
    if hide_dealer:
        dealer_display = ['X'] + dealer_cards[1:]  # Hide first card
        dealer_score = '??'
    else:
        dealer_display = dealer_cards        

    print(f"{player_text} {player.get_cards()}, current score: {player.get_cards_total()}")
    print(f"{dealer_text} {dealer_display}, current score: {dealer_score}\n")

    logger.info(f"{player_text} {player.get_cards()}, current score: {player.get_cards_total()}")
    logger.info(f"{dealer_text} {dealer_display}, current score: {dealer_score}\n")


def initial_deal()-> None:
    '''
    Perform initial card assignments to the player and the dealer.
    '''
    # deal user two cards
    logger.info("Dealer performs initial deal.")
    player.set_cards(deal(2, bjc.CARDS_LIST, player.get_cards()))
    
    # deal dealer one card
    dealer.set_cards(deal(1, bjc.CARDS_LIST, dealer.get_cards()))

    display_current_cards_and_totals("Your cards: ", "Dealer's first cards: ")


def check_winner()->None:
    '''
    Check the winner after each round of play.
    '''
    logger.info("Playing and checcking the winner.")
    while True:
        player_total = player.get_cards_total()
        dealer_total = dealer.get_cards_total()

        if player_total == 21 and dealer_total == 21:
            print('Draw!!!')
            logger.info("Draw!!!")
            break # draw - double blackjack

        # no winner
        if player_total <= 21 and dealer_total <= 21:
            choice = input("Type 'y' to get another card, type 'n' to pass (q to quit): ").strip().lower()

            if choice == "q":
                exit_program(bjc.EXIT_MESSAGE)

            elif choice == "y": # player hit
                player.set_cards(deal(get_deal_amount(), bjc.CARDS_LIST, player.get_cards()))
            
            else: # player stay current hand, dealer hit
                dealer.set_cards(deal(get_deal_amount(), bjc.CARDS_LIST, dealer.get_cards()))

            display_current_cards_and_totals("Your Cards: ", "Dealer's Cards: ", hide_dealer=False)
            continue
    
        if player_total > 21:
            # dealer wins
            print('You went over. You lose. \U0001F923')
            logger.info('You went over. You lose. \U0001F923')
            break
        else:
            # player wins
            print(f"Opponent went over. You win!!!. \U0001f600")
            logger.info('Opponent went over. You win!!!. \U0001f600')
            break
    

def reset_card_lists()->None:
    '''
    Clears the cards list for the player and dealer to have empty list at the 
    start of each new game of Blackjack.
    '''
    logger.info("Resetting card lists.")
    player.reset()
    dealer.reset()

    logger.info(f"Player's cards: {player.get_cards()} | Player's cards total: {player.get_cards_total()} ")
    logger.info(f"Dealer's cards: {dealer.get_cards()} | Dealer's cards total: {dealer.get_cards_total()} ")


def exit_program(message, code=0):
    '''
    Centralized exit function to handle the program termination.

    Args:
            message (str): Message to display and log when exiting.
            code (int): Exit code (0 for normal exit, 1 for errors).
    '''
    logger.info(message)
    sys.exit(message)


def main()-> None:
    """ Main function to start the blackjack program. """
    try:
        logger.info('Starting the blackjack game.')
        while True: 
            choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n' (q to quit): ").strip().lower()

            if choice == "q":
                exit_program(bjc.EXIT_MESSAGE)

            elif choice == "y":
                print(art.logo)                      
                initial_deal()
                check_winner()
                reset_card_lists()
            else:
                return            

    except ValueError as ex:
        logger.error(f"ValueError: {ex}")

    except TypeError as ex:
        logger.error(f"TypeError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{bjc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main BlackJack function.")


if __name__ == "__main__":
    main()