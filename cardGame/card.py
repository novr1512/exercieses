class card:
    suits = ["spades","hearts","diamonds", "clubs"]
        
    values = [None, None,"2", "3","4", "5", "6", "7","8", "9", "10","Jack", "Queen","King", "Ace"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


    def _cmp (self, value):
        '''
        Compare the two non-NaN decimal instances self and other.
        Returns -1 if self < other, 0 if self == other and 1
        if self > other.    
        '''
        
        if self.value == value.value:
            if self.suit < value.suit:
                return -1
            elif self.value == value.value:
                return 0
            else :
                return 1
        elif self.value < value.value:
            return -1
        else:
            return 1

    def __gt__ (self, value):
        return self._cmp (value) > 0

    def __ge__ (self, value):
        return self._cmp (value) >= 0

    def __lt__ (self, value):
        return self._cmp (value) < 0

    def __le__ (self, value):
        return self._cmp (value) <= 0

    def __repr__(self):
        v = str(self.values[self.value]) + " of " + str(self.suits[self.suit])
        return v
