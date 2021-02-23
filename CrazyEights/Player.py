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

    def addOneToPlayerHand(self,aCard):
        self.playerHand.append(aCard)