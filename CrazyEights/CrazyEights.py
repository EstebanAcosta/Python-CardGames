players = []
from Suits import*
from Ranks import*
from Card import*
from Player import*
from Deck import*

def setUpPlayers():
    print("How many players do you want in this game?\n")


def addPlayers(player):
    players.append(player)

def setUpGame():
    pass

def startGame():
    print("Welcome to Crazy Eights \n")

def run():
    setUpPlayers()
    setUpGame()
    startGame()

run()