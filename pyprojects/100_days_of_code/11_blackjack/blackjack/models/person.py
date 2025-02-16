class Person:

    __cards:list[int]           # private attribute


    def __init__(self):
        """Constructor initialize object."""
        self.__cards = []


    def get_cards(self):
        """Return a copy of the current cards list."""
        return self.__cards.copy() # Return a copy to prevent direct modification


    def set_cards(self, cards_list:list[int])->None:
        """
        Updates the current cards list with new cards_list.

        Args:
                cards_list (list[int]): The new cards list to set objects cards list to.
        """
        if not isinstance(cards_list, list) or not all(isinstance(card, int) for card in cards_list):
            raise TypeError("Invalid Type: cards_list must be a list of integers.")

        self.__cards = cards_list


    def get_cards_total(self)->int:
        """
        Retrieve the sum of the current cards list items.

        Returns:
                int: The sum of the current cards list.
        """
        return sum(self.__cards)  # Accessing private attribute internally