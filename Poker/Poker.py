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
    rounds = 0
    minRounds = 1
    maxRounds = 3
    inputRounds = ""
    # continue looping until user inputs a number for number rounds that is between the min and the max
    while rounds < minRounds or rounds > maxRounds:
        inputRounds = input("Please enter a number for number of rounds that's more than or equal to " + str(
            minRounds) + " and less than or equal to " + str(maxRounds) + "\n")
        # if player input isn't a number
        while re.match("[0-9]+$", inputRounds) == None:
            # Display the error message and ask player for input
            inputRounds = input("Please enter a number for rounds\n")
        # convert the input into an integer
        rounds = int(inputRounds)
    print("__________________________________________________________________________")
    startGame(deck, rounds)

def startGame(deck,rounds):
    # randomly select a player to start the game
    whoseTurn = random.randint(0, len(players) - 1)
    # set the current round to 0
    currentRound = 0

        # continue looping until there are no more rounds left
    while currentRound < rounds:
        # shuffle the deck
        deck.shuffle()

        # continue looping until the game is over
        while endGame(deck) == False:
            whoseTurn = whoseTurnIsIt(whoseTurn)

        currentRound+=1

        # print the round results and determine who gets to go next
        whoseTurn = getGameResults(currentRound) - 1

        # loop through each player
        for player in players:
            # clear each player's hand
            player.clearHand()

        # reset the deck
        deck = Deck()

        deck.shuffle()

        howManyCardsEachPlayerNeeds =  5
        # loop through the players
        for i in range(len(players)):
            # draw multiple cards from the deck and add it to the player's hand
            players[i].setPlayerHand(deck.drawMultiple(howManyCardsEachPlayerNeeds))

def getGameResults(round):
    #create a ranks object
    rank = Ranks()
    #get the dictionary of ranks in the ranks class
    ranks = rank.getRanks()

    print("Results Of Round " + str(round) + ":\n")
    winner = ""
    minScore = 0

    #loop through each player in the list of players
    for player in players:
        #set score to 0
        score = 0
        #loop through each card in the player's hand
        for card in player.getPlayerHand():
            #Take the card's rank, search the value associated with that rank in the ranks dictionary and add it to the total score
            score+=ranks[card.getRank()]
        player.addToCurrentScore(score)
        print(player.getName() + " scored " + str(score) + " points this round\n")
        print("_______________________________________________________________________\n")

    #set the winner to some random player
    winner = players[0]
    #set the minimum score to the random player's current score
    minScore = players[0].getCurrentScore()

    #Loop through each player
    for player in players:
        #If this player's current score is less than the minimum score
        if player.getCurrentScore() < minScore:
            #set that player to be the winner
            winner = player
            #set the minimum score to be the player's current score
            minScore = player.getCurrentScore()

    print("Winner of Round " + str(round + 1) + " is " + winner.getName() + " with " + str(winner.getCurrentScore()) + " points")
    print("_______________________________________________________________________")
    return winner.getPlayerID()

def endGame(deck):

    if deck.getDeckSize() == 0:
        return True

    for player in players:
        if player.getCurrentScore() == 100:
            return True
    return False

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