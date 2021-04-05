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

    def clearHand(self):
        self.__playerHand.clear()

    def containsThisCard(self,thisCard):
        for eachCard in self.__playerHand:
            if eachCard == thisCard:
                return True
        return False

    def getCard(self,position):
        return self.__playerHand[position - 1]

    def hasRoyalFlush(self):
        pass

    def hasStraightFlush(self):
        pass

    def hasFourOfKind(self):
        pass

    def hasFullHouse(self):
        pass

    def hasFlush(self):
        pass

    def hasStraight(self):
        pass

    def hasThreeOfKind(self):
        pass

    def hasTwoPair(self):
        pass

    def hasPair(self):
        pass

    def hasHighCard(self):
        pass

    def numTimesRankAppears(self):
        ranks = self.getAllRanksPlayerHas()

        return {rank : self.__playerHand.count(rank) for rank in ranks}

    def numTimesSuitAppears(self):
        suits = self.getAllSuitsPlayerHas()

        return {suit : self.__playerHand.count(suit) for suit in suits}

    def getAllRanksPlayerHas(self):
        ranks = []
        for card in self.__playerHand:
            if card.getRank() not in ranks:
                ranks.append(card.getRank())
        return ranks

    def getAllSuitsPlayerHas(self):
        suits = []
        for card in self.__playerHand:
            if card.getSuit() not in suits:
                suits.append(card.getSuit())
        return suits

    def showPlayerCards(self):
        print(self.getName() + "'s Hand: ")
        position = 1
        for card in self.getPlayerHand():
            print(str(position)+ ": " + "( "  + card.__str__() + " )")
            position+=1
        print()


