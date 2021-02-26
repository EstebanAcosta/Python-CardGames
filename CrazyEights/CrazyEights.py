from Suits import*
from Ranks import*
from Card import*
from Player import*
from Deck import*
import re
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
    min = 2
    max = 5

    while numPlayers < min or numPlayers > max:
        inputNumPlayers =input("Please keep the number of players between " + str(min) + " and " + str(max) + "\n")

        while not re.match("[0-9]+",inputNumPlayers):
           inputNumPlayers = input("Please enter a number\n")

        numPlayers = int(inputNumPlayers)

    addPlayers(numPlayers)

    print(str(numPlayers) + " players have been added to the game\n")

    print("_____________________________________________________________")

def setUpPlayers():
    deck = Deck()

    deck.shuffle()

    howManyCardsEachPlayerNeeds = 0
    if len(players) == 2:
        howManyCardsEachPlayerNeeds = 7
    else:
        howManyCardsEachPlayerNeeds = 8


def setUpGame():
    pass

def startGame():
    pass

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
    setUpGame()
    startGame()

run()