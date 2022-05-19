import random

class Cards:
    """Pre-defined variables in __init__ allocates memory size early which makes the program run efficiently
    Methods:
        def __init__(self):
            self.card1 & self.card2 are pre-defined card values to be used later
        def get_new_card(self):
            if player answers yes to play again in the director.py file, then overwrite the new card1 with the value of the old card2 from the prior round
            "self.card2" creates the new card2 value as a random number between 1 and 13 inclusive
    """
    def __init__(self):
        """Constructs a new Director.
        Args: self (Director): an instance of Director. """
        # pre-defined both card values as zero to be used later
        self.card1 = 0
        self.card2 = 0
        
    def get_card_value(self):
        """Gets both card values as a random number
        Args: self (Director): an instance of Director. """
        # creates both card values as a random number between 1 and 13 inclusive
        self.card1 = random.randint(1,13)
        self.card2 = random.randint(1,13)

    def get_new_card(self):
        """Saves card2 as the first card in the next round, then creates a new random number for card2 in the next round
        Args: self (Director): an instance of Director. """
        # if player answers yes to play again in the director.py file, then overwrite the new card1 with the value of the old card2 from the prior round
        self.card1 = self.card2
        # creates the new card2 value as a random number between 1 and 13 inclusive
        self.card2 = random.randint(1,13)