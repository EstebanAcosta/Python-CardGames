class Player:
    def __init__(self,id):
        self.setPlayerID(id)
        self.setPlayerHand([])
        self.setName("")
        self.setCurrentScore(0)

    def setPlayerID(self,id):
        self.__id = id

    def getPlayerID(self):
        return self.__id

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name

    def getPlayerHand(self):
        return self.__playerHand

    def setPlayerHand(self,playerHand):
        self.__playerHand = playerHand

    def setCurrentScore(self, score):
        self.__current_score = 0

    def getCurrentScore(self):
        return self.__current_score

    def addToCurrentScore(self, score):
        self.__current_score += score

    def getPlayerHandSize(self):
        return len(self.__playerHand)

    def addMultipleToPlayerHand(self,moreCards):
        self.__playerHand.extend(moreCards)

    def addOneToPlayerHand(self,oneCard):
        self.__playerHand.append(oneCard)

    def removeOneFromPlayerHand(self,position):
        return self.__playerHand.pop(position - 1)

    def removeMultipleFromPlayerHand(self,newCards):
        for card in newCards:
            for playerCard in self.__playerHand:
                if card == playerCard:
                    self.__playerHand.remove(playerCard)

    def containsThisCard(self,thisCard):
        for eachCard in self.__playerHand:
            if eachCard == thisCard:
                return True
        return False

    def getCard(self,position):
        return self.__playerHand[position - 1]

    def hasMatchingCard(self,topCard):
        for card in self.__playerHand:
            if card.getSuit() == topCard.getSuit() or card.getRank() == topCard.getRank() or card.getRank() == "EIGHT":
                return True
        return False

    def showPlayerCards(self):
        print(self.getName() + "'s Hand: ")
        position = 1
        for card in self.getPlayerHand():
            print(str(position)+ ": " + "( "  + card.__str__() + " )")
            position+=1
        print()


