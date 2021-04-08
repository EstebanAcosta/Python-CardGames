from Ranks import*
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
        self.__playerHand = self.__sort(playerHand)

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
       suits = self.numTimesSuitAppears()

       suit = ""

       #loop through the suits dictionary
       for key in suits:
           #if the # of times the suit appears is the same as the number of cards in the player's hand
           #in other words if there are five cards with the same suit
           if suits[key] == len(self.__playerHand):
                break
           #if there are no five cards that have the same suit
           else:
               return False

       #if the player hand has a ten, jack, queen, king and an ace
       if self.__playerHand[0].getRank() == "TEN" and  self.__playerHand[1].getRank() == "JACK" and self.__playerHand[2].getRank() == "QUEEN"  and self.__playerHand[3].getRank() == "KING" and self.__playerHand[4].getRank() == "ACE":
            return True

       return False

    def hasStraightFlush(self):
        suits = self.numTimesSuitAppears()

        suit = ""

        # loop through the suits dictionary
        for key in suits:
            # if the # of times the suit appears is the same as the number of cards in the player's hand
            # in other words if there are five cards with the same suit
            if suits[key] == len(self.__playerHand):
                break
            # if there are no five cards that have the same suit
            else:
                return False

        for i in range(len(self.__playerHand) - 1):
            if self.__playerHand[i].getRankValue() + 1 != self.__playerHand[i].getRankValue():
                return False

        return True

    def hasFourOfKind(self):
        return False

    def hasFullHouse(self):
        return False

    def hasFlush(self):
        return False

    def hasStraight(self):
        return False

    def hasThreeOfKind(self):
        return False

    def hasTwoPair(self):
        return False

    def hasPair(self):
        return False

    def hasHighCard(self):
        return False

    def __sort(self,playerHand):

        rank = Ranks().getRanks()

        # Traverse through all array elements
        for i in range(len(playerHand)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(playerHand)):
                if self.__playerHand[min_idx].getRank() > self.__playerHand[j].getRank():
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            self.__playerHand[i], self.__playerHand[min_idx] = self.__playerHand[min_idx], self.__playerHand[i]

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


