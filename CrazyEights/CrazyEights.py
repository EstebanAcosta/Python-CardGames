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
    pass

def setUpGame():
    pass

def startGame():
    pass

def run():
    setUpNumPlayers()
    setUpPlayers()
    setUpGame()
    startGame()

run()