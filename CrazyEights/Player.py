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

    def