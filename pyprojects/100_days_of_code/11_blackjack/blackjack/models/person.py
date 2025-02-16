class Person:

    cards:list[int]
    card_total:int
    
    def __init__(self):
        self.cards = []
        self.card_total = 0

    def get_cards(self):
        return self.cards

    def set_cards(self, cards_list:list[int])->None:
        self.cards = cards_list

    def get_cards_total(self)->int:
        return sum(self.cards)

    def set_cards_total(self, total)-> None:
        self.card_total = total