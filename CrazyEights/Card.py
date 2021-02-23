class Card:

    rank = ""
    suit = ""

    def __init__(self,rank,suit):
        self.setRank(rank)
        self.setSuit(suit)

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def setSuit(self,suit):
        self.suit = suit

    def setRank(self,rank):
        self.rank = rank

    def __eq__(self, other):
        if other == None:
            return False
        return self.rank == other.rank and self.suit == other.suit


    def __str__(self):
        if len(self.suit) != 0:
            return self.getRank() + " of " + self.getSuit()
        else:
            return self.getRank()
