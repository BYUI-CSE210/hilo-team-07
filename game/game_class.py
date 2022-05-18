from game.card_class import Cards

class Game():
    """Pre-defined variables in __init__ allocates memory size early which makes the program run efficiently
    Game does following:
       1. displays 1st card's value
       2. asks player to guess if next card willb be hiher or lower than first card
       3. display 2nd card's value
       4. increases score by 100pts if player was correct or decreases by 75pts if player was wrong
    Methods:
        def __init__(self):
            "self.player_score" is player's first score at beginning of game
            "self.cards" calls "Cards" class & saves it into a variable
            "self.cards.get_card_value()" calls "Cards" class's get_card_value method to save both cards' values
        def display_card(self):
            "player_guess" asks player to guess if card2 will be higher or lower than card1
            "Validation Section" checks if player guesses H/L correct & increase or decrease score accordingly 
    """
    
    def __init__(self):
        """Constructs a new Director. 
        Args: self (Director): an instance of Director. """
        # the player's first score at the beginning of the game
        self.player_score = 300
        # calls the "Cards" class & saves it into a variable
        self.cards = Cards()
        # calls the "Cards" class's get_card_value method to save both cards' values
        self.cards.get_card_value()

    # Method from the Game Class
    def display_card(self):
        """Display the first card's value, then asks if the next card is higher or lower. Then display the 2nd card's value. Then increases or decreases the score accordingly 
        Args: self (Director): an instance of Director. """
        print()
        print(f'The card is: {self.cards.card1}')
        player_guess = input('Will the next card be higher or lower? [H/L]: ')
        print(f'The next card is: {self.cards.card2}')
       
        # This is the Validation Section
        # checks if player guesses higher and is correct, then adds 100pts to their score
        if player_guess.upper() == 'H' and self.cards.card2 > self.cards.card1:
            self.player_score += 100
        # checks if player guesses lower and is correct, then adds 100pts to their score
        elif player_guess.upper() == 'L' and self.cards.card2 < self.cards.card1:
            self.player_score += 100
        else: 
            self.player_score -= 75

        print(f'Your score is: {self.player_score}')
        # game over message when player's score is equal to 0 
        if self.player_score <= 0:
            print('Game over!')
        self.cards.get_new_card()
        return self.player_score
        