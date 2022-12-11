from random import shuffle
from card import card

class deck:
    def __init__(self):
        self.cards=[]

        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(card(j,i))
        shuffle(self.cards)

    def rm_card(self):
        try:
            return self.cards.pop(0)
        except:
            return None