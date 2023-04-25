import os
import random

from art import logo, card_art

os.system('clear')

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_deck   = {
    'num' : [],
    'art' : []
}
computer_deck = {
    'num' : [],
    'art' : []
}

finished = False

def dealCard():
    return random.choice( cards )

def getTotal( deck ):
    if sum( deck['num'] ) >= 21:
        for i, card in enumerate( deck['num'] ):
            if card == 11:
                deck['num'][i] = 1
                
    return sum( deck['num'] )

def checkScores():
    global finished
    
    if getTotal( player_deck ) >= 21 or getTotal( computer_deck ) >= 21:
        finished = True

    print(f'    Your final hand: { player_deck }, final score: { getTotal( player_deck ) }')
    print(f'    Computer\'s final hand: { computer_deck }, final score: { getTotal( computer_deck ) }')

def appendCard( deck ):
    card = dealCard()
    deck['num'].append( card )
    deck['art'].append( random.choice( card_art[ str( card ) ] ) )

def startGame():
    global player_deck
    global computer_deck
    global finished

    finished = False

    player_deck   = { 'num' : [], 'art' : [] }
    computer_deck = { 'num' : [], 'art' : [] }

    appendCard( player_deck )
    appendCard( player_deck )

    appendCard( computer_deck )
    appendCard( computer_deck )

    while not finished:
        printBoard()
        getCard = input("\n    Type 'y' to get another card, type 'n' to pass: ").lower()
        if getCard == 'y':
            appendCard( player_deck )

        if getTotal( computer_deck ) < 17 and getTotal( player_deck ) < 21:
            appendCard( computer_deck )

        elif getTotal( computer_deck ) >= 17 and getCard == 'n':
            finished = True

        checkScores()
    else:
        os.system('clear')
        print( logo )

        if getTotal( player_deck ) >= 21 or getTotal( player_deck ) < getTotal( computer_deck ):
            print('\n    YOU LOST\n')

        elif getTotal( computer_deck ) >= 21 or getTotal( player_deck ) > getTotal( computer_deck ):
            print('\n    YOU WIN!\n')

        else:
            print('\n    YOU\'RE EVEN\n')

        print(f'    Your final hand: { "  ".join(player_deck["art"]) }')
        print(f'    Final score: { getTotal( player_deck ) }')
        print(f'\n    Computer\'s final hand: { "  ".join(computer_deck["art"]) }')
        print(f'    Final score: { getTotal( computer_deck ) }')

        input('\n    Press ENTER to play again\n    ')
        startGame()

def printBoard():
    os.system('clear')

    print( logo )
    string = '\n    '
    for key in card_art:
        if key == '1':
            string += f'{ card_art[ key ][0] } = { key }/11 '
        elif not key == '11':
            string += f'{ card_art[ key ][0] } = { key } '

    print( string )
    print(f'\n    Computer\'s fist card: { computer_deck["art"][0] }')
    print(f'\n    Your cards: { "  ".join(player_deck["art"]) }')
    print(f'    Current score: { getTotal( player_deck ) }')

print( logo )
print('\n    Do you want to play a game of Blackjack?')
input('    Press ENTER to start the game!\n    ')
startGame()