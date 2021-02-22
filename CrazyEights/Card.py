class Card:

    def __init__(self,rank,suit):
        self.rank = rank

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def setSuit(self,suit):
        self.suit = suit

    def __str__(self):

        if self.getSuit() != None:
            return self.getSuit() + " " + self.getRank()

