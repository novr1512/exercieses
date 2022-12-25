from Deck import Deck
from Player import Player


class Game :

    def __init__(self,player1name,player2name):

        self.player1= Player(player1name)
        self.player2= Player(player2name)

        self.Deck = Deck()

    def wining(self,player1name,player2name):
        if(player1name.wins > player2name.wins):
            print(player1name.username + " won the game with the score of "+ str(player1name.wins))
        else:
            print(player2name.username + " won the game with the score of "+ str(player2name.wins))


    def play_game(self):
        response = 'c'
        while(len(self.Deck.cards)>1 and response != 'q' and response != 'Q'):

           self.player1.card = self.Deck.rm_card()
           self.player2.card = self.Deck.rm_card()

           print(self.player1.username +" got the card "+str(self.player1.card))
           print(self.player2.username +" got the card "+str(self.player2.card))

           if(self.player1.card > self.player2.card):
                self.player1.wins += 1
                print(self.player1.username + " won")
           else:
                self.player2.wins += 1
                print(self.player2.username + " won")

           response = input("enter q if you want to quit and any other letter if you want to continue:")

        print("game is over")
        self.wining(self.player1,self.player2)


# START THE GAME
player1name = input("enter player 1's username:")
player2name = input("enter player 2's username:")

Game = Game(player1name,player2name)

Game.play_game()
