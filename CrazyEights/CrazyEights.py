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
    #set up the deck
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
    minRounds = 1
    maxRounds = 3
    inputRounds = ""
    #continue looping until user inputs a number for number rounds that is between the min and the max
    while rounds < minRounds or rounds > maxRounds:
        inputRounds = input("Please enter a number for number of rounds that's more than or equal to " + str(minRounds) + " and less than or equal to " + str(maxRounds) + "\n")
        #if player input isn't a number
        while re.match("[0-9]+$",inputRounds) == None:
            #Display the error message and ask player for input
            inputRounds = input("Please enter a number for rounds\n")
        #convert the input into an integer
        rounds = int(inputRounds)
    print("__________________________________________________________________________")
    startGame(deck,rounds)

def startGame(deck,rounds):
    print("Crazy Eights\n")
    #randomly select a player to start the game
    whoseTurn = random.randint(0,len(players) - 1)
    #set the current round to 0
    currentRound = 0
    #create an empty discard pile
    discardPile = []

    #continue looping until there are no more rounds left
    while currentRound < rounds:
        # shuffle the deck
        deck.shuffle()
        # draw a card from the deck and add it to the discard pile
        discardPile.append(deck.drawOne())
        # continue looping until we get a card that doesn't have an eight on it
        while discardPile[len(discardPile) - 1].getRank() == "EIGHT":
            # clear the discard pile
            discardPile.clear()
            # reset the deck
            deck = Deck()
            # shuffle the deck
            deck.shuffle()
            # pick up the top card of the deck and put it in the discard pile
            discardPile.append(deck.drawOne())

        #continue looping until the game is over
        while endGame(deck) == False:
            topCard = discardPile[len(discardPile) - 1]
            print("Round " + str(currentRound + 1))
            print("Player " + str(players[whoseTurn].getPlayerID()) + " " + players[whoseTurn].getName() + "'s Turn\n")
            print("Discard Pile: " + topCard.__str__() + "\n")
            players[whoseTurn].showPlayerCards()

            whichCard = 0
            thatCard = ""
            selectedCard = ""

            #if the current player has card in their hand whose rank or suit matches the top card's rank or suit or if they have a wild card
            if players[whoseTurn].hasMatchingCard(topCard):
                #continue looping until the player selects a card that is within the range of cards and their card's rank or suit matches the top card's rank or suit
                 while whichCard < 1 or whichCard > len(players[whoseTurn].getPlayerHand()) or (selectedCard.getRank() != topCard.getRank() and selectedCard.getSuit() != topCard.getSuit() and selectedCard.getRank() != "EIGHT"):
                        #If the selected card isn't a valid card number, print this error message
                        if whichCard < 1 or whichCard > len(players[whoseTurn].getPlayerHand()):
                            thatCard = input("Please enter a valid card number between 1 and " + str(len(players[whoseTurn].getPlayerHand())) + "\n")
                        #If the selected card doesn't match with the top card, print this error message
                        else:
                            thatCard = input("Please select a card whose rank or suit matches the top card's rank or suit or is an eight\n")
                        # Continue looping until user inputs a whole number
                        while re.match("[0-9]+$", thatCard) == None:
                             thatCard = input("Please enter a card number\n")
                        # Convert string input into an integer
                        whichCard = int(thatCard)
                        #store the card that the player selected
                        if whichCard >= 1 and whichCard <= len(players[whoseTurn].getPlayerHand()):
                             selectedCard = players[whoseTurn].getCard(whichCard)
                 if selectedCard.getRank() == "EIGHT":
                      print("SUITS:")
                      suits = Suits().getSuits()
                      #print the suits along with their position
                      for position, suit in enumerate(suits):
                          print(str(position + 1) + ": " + suit )
                      print()
                      whichSuit =  0
                      thatSuit = ""
                      #if suit position is less than 1 or greater than4 (if it's out of bounds)
                      while whichSuit < 1 or whichSuit > 4:
                          thatSuit = input("Please enter a number between 1-4 to choose the suit you want to change this card to\n")
                          #if the input isn't a numerical value
                          while re.match("[0-9]+$", thatSuit) == None:
                              thatSuit = input("Please enter a number\n")
                         #convert the string input to an integer
                          whichSuit = int(thatSuit)
                      #remove the selected card from the player's hand
                      players[whoseTurn].removeOneFromPlayerHand(whichCard)
                      #change the selected card's rank to the one the player just chose
                      selectedCard.setSuit(suits[whichSuit - 1])
                      #add the modified selected card to the discard pile
                      discardPile.append(selectedCard)
                 else:
                    #Add the last card the player added to their hand to the discard pile
                    discardPile.append(players[whoseTurn].removeOneFromPlayerHand(whichCard))
            else:
                drawnCard = ""
                #continue looping until there's a card from the deck
                while players[whoseTurn].hasMatchingCard(topCard) == False and deck.getDeckSize() != 0:
                    #draw one card from the deck and store it in a var
                    drawnCard = deck.drawOne()
                    #Add the drawn card to the player's hand
                    players[whoseTurn].addOneToPlayerHand(drawnCard)
                    #print the drawn card
                    print("Drawn Card: " + drawnCard.__str__())
                    print("______________________________________________")
                    nextInput = ""
                    #Continue pressing n until the next drawn card matches with the top card
                    while nextInput != "n":
                        nextInput = input("Press n for next\n")


                if drawnCard.getRank() == "EIGHT":
                    print("SUITS:")
                    suits = Suits().getSuits()
                    # print the suits along with their position
                    for position, suit in enumerate(suits):
                        print(str(position + 1) + ": " + suit)
                    print()
                    whichSuit = 0
                    thatSuit = ""
                    # if suit position is less than 1 or greater than4 (if it's out of bounds)
                    while whichSuit < 1 or whichSuit > 4:
                        thatSuit = input(
                            "Please enter a number between 1-4 to choose the suit you want to change this card to\n")
                        # if the input isn't a numerical value
                        while re.match("[0-9]+$", thatSuit) == None:
                            thatSuit = input("Please enter a number\n")
                        # convert the string input to an integer
                        whichSuit = int(thatSuit)
                    # remove the selected card from the player's hand
                    players[whoseTurn].removeOneFromPlayerHand(players[whoseTurn].getPlayerHandSize())
                    # change the selected card's rank to the one the player just chose
                    drawnCard.setSuit(suits[whichSuit - 1])
                    # add the modified selected card to the discard pile
                    discardPile.append(drawnCard)
                else:
                    discardPile.append(players[whoseTurn].removeOneFromPlayerHand(players[whoseTurn].getPlayerHandSize()))

                # if the deck is empty
                if deck.getDeckSize() == 0:
                    continue

            #change turns
            whoseTurn = whoseTurnIsIt(whoseTurn)
            print("________________________________________________________________________________________________________")

        #print the round results and determine who gets to go next
        whoseTurn = getGameResults(currentRound) - 1

        #loop through each player
        for player in players:
            #clear each player's hand
            player.clearHand()

        #reset the deck
        deck = Deck()

        deck.shuffle()

        #reset the discard pile
        discardPile.clear()

        howManyCardsEachPlayerNeeds = 0

        if len(players) == 2:
            howManyCardsEachPlayerNeeds = 7
        else:
            howManyCardsEachPlayerNeeds = 8

        # loop through the players
        for i in range(len(players)):
            # draw multiple cards from the deck and add it to the player's hand
            players[i].setPlayerHand(deck.drawMultiple(howManyCardsEachPlayerNeeds))

        #add one to the current round
        currentRound += 1

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


#Determine who's going next in the game
def whoseTurnIsIt(whoseTurn):
    if whoseTurn + 1 == len(players):
        return 0
    else:
        whoseTurn+=1
    return whoseTurn


#End game once at least one has gotten rid of all their cards
#Or if the deck is empty
def endGame(deck):
    for player in players:
        if player.getPlayerHandSize() == 0:
            return True
    if deck.getDeckSize() == 0:
        return True
    return False

#main method
def run():
    setUpNumPlayers()
    setUpPlayers()
run()