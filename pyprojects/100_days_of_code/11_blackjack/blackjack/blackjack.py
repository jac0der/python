'''
    Create a black jack game.

    @datetime:: February 12, 2025 8:03 pm (UTC-5)
    @author:: jac0der
'''
import sys
import os
import random
import blackjack_enum as bje
import blackjack_constants as bjc

# Add the 'logging' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../logging')))
import jaclog
logger = jaclog.configure('blackjack', './blackjack.log')


# setup data structure to keep track of the player and computer cards and totals.
players_cards: dict[bje.PlayerType, dict] = {
    bje.PlayerType.PLAYER: {
        bjc.CARDS: [],
        bjc.CARD_TOTAL: 0
    },

    bje.PlayerType.COMPUTER: {
        bjc.CARDS: [],
        bjc.CARD_TOTAL: 0
    }
}


def get_deal_amount()->int:
    '''
    Get a random number to be used to determine how many more cards
    shoul;d be dealt wo either player or computer.

    Returns:
            int: The total amount of cards to deal.
    '''
    return random.randint(1, 3)


def deal(deal_amount:int, cards_list:list[int], current_cards:list[int])->list[int]:
    '''
    Update the cards list for either the player or computer with new dealt cards.

    Args:
            deal_amount (int): The amount of cards to deal to player or computer.
            cards_list list[int]: The valid cards to deal from.
            current_cards list[int]: The current cards list for either player or computer.
    Returns:
            list[int]: The updated cards list for the player or computer with newly dealt cards.
    '''
    if not isinstance(deal_amount, int):
        raise ValueError('Invalid Type: Expected an integer for deal_amount.')
    
    for n in range(1, deal_amount + 1):
        card = random.choice(cards_list)
        current_cards.append(card)

    return current_cards
    

def initial_deal()-> None:
    '''
    Perform initial card assignments to the player and the computer.
    '''
    # deal user two cards
    players_cards[bje.PlayerType.PLAYER][bjc.CARDS] = deal(2, bjc.CARDS_LIST, players_cards[bje.PlayerType.PLAYER][bjc.CARDS])
    players_cards[bje.PlayerType.PLAYER][bjc.CARD_TOTAL] = sum(players_cards[bje.PlayerType.PLAYER][bjc.CARDS])

    # deal computer one card
    players_cards[bje.PlayerType.COMPUTER][bjc.CARDS] = deal(1, bjc.CARDS_LIST, players_cards[bje.PlayerType.COMPUTER][bjc.CARDS])
    players_cards[bje.PlayerType.COMPUTER][bjc.CARD_TOTAL] = sum(players_cards[bje.PlayerType.COMPUTER][bjc.CARDS])
    
    print(f"Your cards: {players_cards[bje.PlayerType.PLAYER][bjc.CARDS] }, current score: {players_cards[bje.PlayerType.PLAYER][bjc.CARD_TOTAL]}")
    print(f"Computer's first card: {players_cards[bje.PlayerType.COMPUTER][bjc.CARDS]}, current score: {players_cards[bje.PlayerType.COMPUTER][bjc.CARD_TOTAL]}")


def check_winner():
    pass


def main()-> None:
    """ Main function to start the blackjack program. """
    try:
        logger.info('Starting the blackjack game.')
        initial_deal()


    except ValueError as ex:
        logger.error(f"ValueError: {ex}")

    except (KeyboardInterrupt, EOFError):
        print(f"\n{bjc.EXIT_MESSAGE}")
        return

    except Exception:
        logger.exception("Error occurred in main BlackJack function.")


if __name__ == "__main__":
    main()