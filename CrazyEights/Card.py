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

    def __str__(self):
        if len(self.suit) != 0:
            return self.getSuit() + " " + self.getRank()
        else:
            return self.getRank()
