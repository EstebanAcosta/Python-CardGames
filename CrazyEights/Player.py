class Player:
    id = 0
    name = ""
    playerHand = []

    def __init__(self,id):
        self.setPlayerID(id)

    def setPlayerID(self,id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getPlayerHand(self):
        return self.playerHand

    def setPlayerHand(self,playerHand):
        self.playerHand = playerHand

    def getPlayerHandSize(self):
        return len(self.playerHand)

    def addMultipleToPlayerHand(self,moreCards):
        self.playerHand.extend(moreCards)

    def addOneToPlayerHand(self,oneCard):
        self.playerHand.append(oneCard)

    def removeOneFromPlayerHand(self,position):
        return self.playerHand.pop(position - 1)

    def removeMultipleFromPlayerHand(self,newCards):
        for card in newCards:
            for playerCard in self.playerHand:
                if card == playerCard:
                    self.playerHand.remove(playerCard)

    def containsThisCard(self,thisCard):
        for eachCard in self.playerHand:
            if eachCard == thisCard:
                return True
        return False



