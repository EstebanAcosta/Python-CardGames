class Card:
    def __init__(self,rank,suit):
        self.setRank(rank)
        self.setSuit(suit)

    def getRank(self):
        return self.__rank

    def getSuit(self):
        return self.__suit

    def setSuit(self,suit):
        self.__suit = suit

    def setRank(self,rank):
        self.__rank = rank

    def __eq__(self, other):
        if other == None:
            return False
        return self.__rank == other.getRank() and self.__suit == other.getSuit()

    def __str__(self):
        if len(self.__suit) != 0:
            return self.getRank() + " of " + self.getSuit()
        else:
            return self.getRank()
