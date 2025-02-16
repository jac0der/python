from models.person import Person

class Dealer(Person):
    def reset(self)->None:
        self.cards:list[int] = []
        self.card_total:int = 0