from game.game_class import Game

class Director:
    """Pre-defined variables in __init__ allocates memory size early which makes the program run efficiently
    Director does the following:
       1. declares "playing" as true to start a later while loop
       2. calls the "Game" class into a variable "play_game"
       3. calls the "play_game.display_card()" method. The "display_card" method is explained in game_class.py
       4. asks if the player wants to play again & restart the game if yes and ends the game if no
    Attributes:
        def main():
            "play_game.display_card()" The "display_card" method is explained in game_class.py
            "player_question" asks player to if they want to play again
            "if player_question.upper() == 'Y':" continues the loop to restart the game
            "else" ends the game when player does not want to play again 
    """
    def __init__(self):
        # pre-defined the following variables to be used later
        self.playing = True
        self.play_game = None
        self.player_question = None

    # This is the main function that contains the game
    def main():
        playing = True
        play_game = Game()

        # while loop to check if the game is playing
        while playing:
            play_game.display_card()
            
            # asks the player if they want to play again
            player_question = input('Do you want to play again? [Y/N] ')
            # if the player wants to play again then return "playing" as true to continue the loop
            if player_question.upper() == 'Y':
                pass
            # if the player does not want to play again then return "playing" as false to end the loop
            else:
                print("Thank you for playing!")
                print()
                playing = False
            
    #Calling the main function
    if __name__ == "__main__":
        main()