'''
    Create a black jack game.

    @datetime:: February 12, 2025 8:03 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
import art
import random
import blackjack_enum as bje
import blackjack_constants as bjc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../logging')))
import jaclog
logger = jaclog.configure('blackjack', './blackjack.log')


# setup data structure to keep track of the player and dealer cards and totals.
players_cards: dict[bje.PlayerType, dict] = {
    bje.PlayerType.PLAYER: {
        bjc.CARDS: [],
        bjc.CARD_TOTAL: 0
    },

    bje.PlayerType.DEALER: {
        bjc.CARDS: [],
        bjc.CARD_TOTAL: 0
    }
}


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

    logger.info(f"Performing deal for deal amount {deal_amount}.")
    
    new_cards = random.sample(cards_list, deal_amount)  # Pick multiple cards at once
    current_cards.extend(new_cards)  # Add to player's current cards

    return current_cards
    

def display_current_cards_and_totals(player_text:str, dealer_text:str)->None:
    '''
    Displays the current cards for player and dealer along with the card totals.

    Args:
            player_text (str): Text to display showing  players cards. e.g. Your Cards:
            dealer_text (str): Text to display showing dealers cards. e.g. Dealers first cards:
    '''
    players_cards[bje.PlayerType.PLAYER][bjc.CARD_TOTAL] = sum(players_cards[bje.PlayerType.PLAYER][bjc.CARDS])
    players_cards[bje.PlayerType.DEALER][bjc.CARD_TOTAL] = sum(players_cards[bje.PlayerType.DEALER][bjc.CARDS])
    print(f"{player_text} {players_cards[bje.PlayerType.PLAYER][bjc.CARDS] }, current score: {players_cards[bje.PlayerType.PLAYER][bjc.CARD_TOTAL]}")
    print(f"{dealer_text} {players_cards[bje.PlayerType.DEALER][bjc.CARDS]}, current score: {players_cards[bje.PlayerType.DEALER][bjc.CARD_TOTAL]}\n")

    logger.info(f"{player_text} {players_cards[bje.PlayerType.PLAYER][bjc.CARDS] }, current score: {players_cards[bje.PlayerType.PLAYER][bjc.CARD_TOTAL]}")
    logger.info(f"{dealer_text} {players_cards[bje.PlayerType.DEALER][bjc.CARDS]}, current score: {players_cards[bje.PlayerType.DEALER][bjc.CARD_TOTAL]}\n")


def initial_deal()-> None:
    '''
    Perform initial card assignments to the player and the dealer.
    '''
    # deal user two cards
    logger.info("Dealer performs initial deal.")
    players_cards[bje.PlayerType.PLAYER][bjc.CARDS] = deal(2, bjc.CARDS_LIST, players_cards[bje.PlayerType.PLAYER][bjc.CARDS])
    
    # deal dealer one card
    players_cards[bje.PlayerType.DEALER][bjc.CARDS] = deal(1, bjc.CARDS_LIST, players_cards[bje.PlayerType.DEALER][bjc.CARDS])

    display_current_cards_and_totals("Your cards: ", "Dealer's first cards: ")


def check_winner()->None:
    '''
    Check the winner after each round of play.
    '''
    logger.info("Playing and checcking the winner.")
    while True:
        player_total = players_cards[bje.PlayerType.PLAYER][bjc.CARD_TOTAL]
        dealer_total = players_cards[bje.PlayerType.DEALER][bjc.CARD_TOTAL]

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
                players_cards[bje.PlayerType.PLAYER][bjc.CARDS] = deal(get_deal_amount(), bjc.CARDS_LIST, players_cards[bje.PlayerType.PLAYER][bjc.CARDS])
            
            else: # player stay current hand, dealer hit
                players_cards[bje.PlayerType.DEALER][bjc.CARDS] = deal(get_deal_amount(), bjc.CARDS_LIST, players_cards[bje.PlayerType.DEALER][bjc.CARDS])

            display_current_cards_and_totals("Your Cards: ", "Dealer's Cards: ")
            continue
    
        if player_total > 21:
            # dealer wins
            print('You went over. You lose. \U0001F923')
            logger.info('You went over. You lose. \U0001F923')
            break
        else:
            # player wins
            print(f"Opponent went over. You win!!!. \U0001f600")
            logger.info('You went over. You lose. \U0001f600')
            break
    

def reset_card_lists()->None:
    '''
    Clears the cards list for the player and dealer to have empty list at the 
    start of each new game of Blackjack.
    '''
    logger.info("Resetting card lists.")
    players_cards[bje.PlayerType.PLAYER] = {bjc.CARDS: [], bjc.CARD_TOTAL: 0}
    players_cards[bje.PlayerType.DEALER] = {bjc.CARDS: [], bjc.CARD_TOTAL: 0}


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

    except (KeyboardInterrupt, EOFError):
        print(f"\n{bjc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main BlackJack function.")


if __name__ == "__main__":
    main()