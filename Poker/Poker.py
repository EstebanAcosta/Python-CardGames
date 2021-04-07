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
    inputNumPlayers = ""
    numPlayers = 0
    minPlayers = 2
    maxPlayers = 4

    print("Welcome to Poker\n")
    print("How many players do you want in this game?")
    print("Minimum number of players is " + str(minPlayers) + " and maximum number of players is " + str(maxPlayers) +"\n")

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
    #set up the deck
    deck = Deck()
    #shuffle the deck
    deck.shuffle()
    #var stores how many cards to deal to each player
    howManyCardsEachPlayerNeeds = 5
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
    startGame(deck)

def startGame(deck):
    # randomly select a player to start the game
    whoseTurn = random.randint(0, len(players) - 1)
    # set the current round to 0
    currentRound = 0

    while endGame():
        pass

def endGame():
    return False

def determineRanking(player):
    if player.hasRoyalFlush():
        return "Royal_Flush"

    elif player.hasStraightFlush():
        return "Straight_Flush"

    elif player.hasFourOfKind():
        return "Four_Of_A_Kind"

    elif player.hasFullHouse():
        return "Full_House"

    elif player.hasFlush():
        return "Flush"

    elif player.hasStraight():
        return "Straight"

    elif player.hasThreeOfKind():
        return "Three_Of_A_Kind"

    elif player.hasTwoPair():
        return "Two_Pair"

    elif player.hasPair():
        return "Pair"

    elif player.hasHighCard():
        return "High_Card"
#Determine who's going next in the game
def whoseTurnIsIt(whoseTurn):
    if whoseTurn + 1 == len(players):
        return 0
    else:
        whoseTurn+=1
    return whoseTurn

#main method
def run():
    setUpNumPlayers()
    setUpPlayers()
run()