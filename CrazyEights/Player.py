class Player:
    def __init__(self,id):
        self.setPlayerID(id)
        self.setPlayerHand([])
        self.setName("")

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
