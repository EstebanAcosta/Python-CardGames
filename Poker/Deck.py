from Suits import*
from Ranks import*
from Card import*
import random
class Deck:
    def __init__(self):
        self.setUpDeck()

    def shuffle(self):
        random.shuffle(self.__deck)
        print("Deck has been shuffled\n")

    def setUpDeck(self):
        deck = []
        suit = Suits()
        rank = Ranks()

        suits = suit.getSuits()
        ranks = rank.getRanks()

        for s in suits:
            for r in ranks:
                deck.append(Card(r,s))

        self.__deck = deck

    def getDeck(self):
        return self.__deck

    def drawOne(self):
        return self.__deck.pop()

    def drawMultiple(self,num):
        cards = []
        for i in range(num):
            cards.append(self.__deck.pop())

        return cards

    def getDeckSize(self):
        return len(self.__deck)

    def __str__(self):
        Deck = ""

        numOfCardsInSuit = 1

        for card in self.__deck:
            if numOfCardsInSuit % 13 == 0:
                Deck += card.__str__() + "\n\n"
                numOfCardsInSuit = 0
            else:
                Deck += card.__str__() + "\n"
            numOfCardsInSuit+=1

        return Deck