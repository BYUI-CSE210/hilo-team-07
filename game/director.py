import random

# Creating a Cards Class
class Cards:
    def __init__(self):
        self.card1 = 0
        self.card2 = 2
        
    def get_card_value(self):
        self.card1 = random.randint(1,13)
        self.card2 = random.randint(1,13)

    def get_new_card(self):
        self.card1 = self.card2
        self.card2 = random.randint(1,13)

# Creating a Game Class
class Game():
    def __init__(self):
        self.player_score = 300
        self.cards = Cards()
        self.cards.get_card_value()

    # Method from the Game Class
    def display_card(self):
        #card_number1 = self.cards.card1
        #card_number2 = self.cards.card2
        print()
        print("The card is: "+ str(self.cards.card1))
        user_guess = input('Higher or lower? [h/l]: ')
        # card_number = random.randint(1,13)
        print('Next card was: ' + str(self.cards.card2))
       
        # This is the Validation Section 
        if user_guess == 'h' and self.cards.card2 > self.cards.card1:
            self.player_score += 100
        elif user_guess == 'l' and self.cards.card2 < self.cards.card1:
            self.player_score += 100
        else: 
            self.player_score -= 75

        print('Your score is: ' + str(self.player_score))

        self.cards.get_new_card()

            

# This is the main function that contains the game

def main():
    playing = True
    user_question = ''
    play1 = Game()

    while playing:
        play1.display_card()
        user_question = input('Play Again? [y/n] ')
        if user_question == 'y':
            #main() 
            pass
        else:
            playing = False
        print()
        
   


#Calling the main function
if __name__ == "__main__":
    main()