from deck import deck
from player import player


class game :

    def __init__(self):

        player1name = input("enter player 1's username:")
        player2name = input("enter player 2's username:")

        self.player1= player(player1name)
        self.player2= player(player2name)

        self.Deck = deck()

    def wining(self,p1,p2):
        if(p1.wins > p2.wins):
            print(p1.username + " won the game with the score of "+ str(p1.wins))
        else:
            print(p2.username + " won the game with the score of "+ str(p2.wins))


    def play_game(self):
        response = 'c'
        while(len(self.Deck.cards)>1 and response != 'q'):

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

           response = input("enter q if you want to quit and :")

        print("game is over")
        self.wining(self.player1,self.player2)


game = game()

game.play_game()
