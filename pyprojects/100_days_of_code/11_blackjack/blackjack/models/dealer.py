from models.person import Person

class Dealer(Person):

    
    def reset(self)->None:
        """Resetting the cars list to empty."""
        self.set_cards([])