from Suits import*
from Ranks import*
from Card import*
from Player import*
from Deck import*
import re
import random

players = []

def addPlayers(howManyPlayers):
    for numPlayer in range(howManyPlayers):
        players.append(Player(numPlayer + 1))

def setUpNumPlayers():
    print("Welcome to Crazy Eights\n")
    print("How many players do you want in this game?")
    print("Minimum number of players is two and Maximum number of players is five\n")

    inputNumPlayers = ""
    numPlayers = 0
    minPlayers = 2
    maxPlayers = 5

    #continue prompting the player until they enter a number that is within the number of players allowed in the game
    while numPlayers < minPlayers or numPlayers > maxPlayers:
        inputNumPlayers =input("Please keep the number of players between " + str(minPlayers) + " and " + str(maxPlayers) + "\n")

        #prompt player again if their input isn't a number
        while re.match("[0-9]+$",inputNumPlayers) == None:
           inputNumPlayers = input("Please enter a whole number\n")

        #convert string input into an integer
        numPlayers = int(inputNumPlayers)

    addPlayers(numPlayers)

    print(str(numPlayers) + " players have been added to the game\n")

    print("_____________________________________________________________")

def setUpPlayers():
    deck = Deck()

    #shuffle the deck
    deck.shuffle()

    #var stores how many cards to deal to each player
    howManyCardsEachPlayerNeeds = 0

    if len(players) == 2:
        howManyCardsEachPlayerNeeds = 7
    else:
        howManyCardsEachPlayerNeeds = 8

    #set a character limit
    limit = 10

    #loop through the players
    for i in range(len(players)):
        #draw multiple cards from the deck and add it to the player's hand
        players[i].setPlayerHand(deck.drawMultiple(howManyCardsEachPlayerNeeds))

        #get player input
        name = input("Please enter a name\n")

        #Until the player puts a name that is within the limit and doesn't have a number in it
        while len(name) > limit or any(char.isdigit() for char in name) == True:

            errorMessage = ""
            #print the error message
            if len(name) > limit :
                errorMessage = "Please enter a name that has less than " + str(limit) + " characters\n"
            else:
                errorMessage = "Please enter a name with no numbers in it\n"
            # continue prompting them
            name = input(errorMessage)

        players[i].setName(name)

        print(players[i].getName() + " has " + str(players[i].getPlayerHandSize()) + " cards")

        print("___________________________________________________________________________")

    setUpGame(deck)

def setUpGame(deck):
    rounds = 0
    minRounds = 3
    maxRounds = 5
    inputRounds = ""
    #continue looping until user inputs a number for number rounds that is between the min and the max
    while rounds < minRounds or rounds > maxRounds:
        inputRounds = input("Please enter a number for number of rounds that's less than " + str(minRounds) + " and more than " + str(maxRounds) + "\n")

        while re.match("[0-9]+$",inputRounds) == None:
            inputRounds = input("Please enter a number for rounds\n")

        rounds = int(inputRounds)

    print("__________________________________________________________________________")
    startGame(deck,rounds)

def startGame(deck,rounds):
    deck = Deck()
    #shuffle the deck
    deck.shuffle()
    print("Crazy Eights\n")
    #randomly select the first player to play the game
    whoseTurn = random.randint(0,len(players) - 1)
    #set the current round to 0
    currentRound = 0
    #create an empty discard pile
    discardPile = []
    #draw a card from the deck and add it to the discard pile
    discardPile.append(deck.drawOne())

    #continue looping until we get a card that doesn't have an eight on it
    while discardPile[len(discardPile) - 1].getRank() == "EIGHT":
        #clear the discard pile
        discardPile.clear()
        #reset the deck
        deck = Deck()
        #shuffle the deck
        deck.shuffle()
        #pick up the top card of the deck and put it in the discard pile
        discardPile.append(deck.drawOne())

    #continue looping until there are no more rounds left
    while currentRound < rounds:
        #continue looping until the game is over
        while endGame() == False:
            topCard = discardPile[len(discardPile) - 1]
            print("Round " + str(currentRound + 1))
            print("Player " + str(players[whoseTurn].getPlayerID()) + " " + players[whoseTurn].getName() + "'s Turn\n")
            print("Discard Pile: " + topCard.__str__() + "\n")
            players[whoseTurn].showPlayerCards()

            whichCard = 0
            thatCard = ""
            selectedCard = ""

            #if the current player has card in their hand whose rank or suit matches the top card's rank or suit
            if players[whoseTurn].hasMatchingCard(topCard):
                 while whichCard < 1 or whichCard > len(players[whoseTurn].getPlayerHand()) or (selectedCard.getRank() != topCard.getRank() and selectedCard.getSuit() != topCard.getSuit()):
                        if whichCard < 1 or whichCard > len(players[whoseTurn].getPlayerHand()):
                            thatCard = input("Please enter a valid card number between 1 and " + str(len(players[whoseTurn].getPlayerHand())) + "\n")
                        else:
                            thatCard = input("Please select a card whose rank or suit matches the top card's rank or suit\n")
                        # Continue looping until user inputs a whole number
                        while re.match("[0-9]+$", thatCard) == None:
                             thatCard = input("Please enter a card number\n")
                        # Convert string input into an integer
                        whichCard = int(thatCard)
                        #store the card that the player selected
                        selectedCard = players[whoseTurn].getCard(whichCard)

            else:
                drawnCard = ""
                #continue looping until there's a card from the deck
                while players[whoseTurn].hasMatchingCard(topCard) == False or deck.getDeckSize() != 0:
                    drawnCard = deck.drawOne()
                    players[whoseTurn].addOneToPlayerHand(drawnCard)

                if deck.getDeck() == 0:
                    pass
                else:
                    discardPile.append(drawnCard)

            #change turns
            whoseTurn = whoseTurnIsIt(whoseTurn)
            break
        currentRound += 1
        break

#Determine who's going next in the game
def whoseTurnIsIt(whoseTurn):
    if whoseTurn + 1 == len(players):
        return 0
    else:
        whoseTurn+=1
    return whoseTurn


#End game once at least one has gotten rid of all their cards
def endGame():
    for player in players:
        if player.getPlayerHandSize() == 0:
            return True
    return False

#main method
def run():
    setUpNumPlayers()
    setUpPlayers()

run()