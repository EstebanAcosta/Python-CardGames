from Suits import*
from Ranks import*
from Card import*

class Deck:

    deck = []

    def __init__(self):
        self.setUpDeck()

    def shuffle(self):
        self.deck.shuffle()
        print("Deck has been shuffled\n")

    def setUpDeck(self):
        deck = []
        suit = Suits()
        rank = Ranks()

        suits = suit.getSuits()
        ranks = rank.getRanks()

        for s in suits:
            for r in ranks:
                deck.append(Card(s,r))

        self.deck = deck


    def draw(self):
        return self.deck.pop()

    def draw(self,num):
        cards = []
        for i in range(num):
            cards.append(self.deck.pop())

        return cards

    def getDeckSize(self):
        return len(self.deck)

    def __str__(self):
        Deck = ""

        numOfCardsInSuit = 1

        for card in self.deck:
            if numOfCardsInSuit % 13 == 0:
                Deck += card.__str__() + "\n\n"
                numOfCardsInSuit = 0
            else:
                Deck += card.__str__() + "\n"
            numOfCardsInSuit+=1

        return Deck