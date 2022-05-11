import random

class Game():
    def __init__(self):
     self.player_score = 300


    def display_card(self):
        card_number1 = random.randint(1,13)
        print()
        print("The card is: "+ str(card_number1))
        user_guess = input('Higher or lower? [h/l]: ')
        card_number = random.randint(1,13)
        print('Next card was: ' + str(card_number))
        if user_guess == 'h' and card_number > card_number1:
            self.player_score += 100
        elif user_guess == 'l' and card_number < card_number1:
            self.player_score += 100
        else: self.player_score -= 75

        print('Your score is: ' + str(self.player_score))

            



def main():
    playing = True
    user_question = ''

    while playing:
        play1 = Game()
        play1.display_card()
        user_question = input('Play Again? [y/n] ')
        if user_question == 'y':
            main()
        else:
            playing == False  
        print()
        
   



if __name__ == "__main__":
    main()
