from Suits import*
from Ranks import*
from Card import*

class Deck:
    deck = []

    def __init__(self):
        self.setUpDeck()

    def shuffle(self):
        self.deck.shuffle()

    def setUpDeck(self):
        deck = []
        suits = Suits()
        ranks = Ranks()

        for suit in Suit:
            for rank in Rank:

    def draw(self):
        return self.deck.pop()

    def draw(self,num):
        cards = []
        for i in range(num):
            cards.append(self.deck.pop())

        return cards

    def getSize(self):
        return len(self.deck)

    def __str__(self):
        Deck = ""

        numOfCardsInSuit = 1

        for card in self.deck:
            if numOfCardsInSuit % 13 == 0:
                Deck += card + "\n\n"
                numOfCardsInSuit = 0
            else:
                Deck += card + "\n"
            numOfCardsInSuit+=1

        return Deck