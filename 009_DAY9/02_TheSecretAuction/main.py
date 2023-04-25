import os
from other import logo, separator

bidders = {}

def askBid():
    os.system('clear')
    global bidders

    print( logo )
    print('Welcome to the Secret Aucion Program.')
    name = input('\nWhat is your name? ').title()
    bid = int( input('What is your bid? $') )

    bidders[ name ] = bid

    more = input("\nAre there any other bidders? Type 'Y' or 'N'. ").lower()
    if more == 'y': 
        askBid()
    else:
        os.system('clear')

        winner = getWinner()

        print( logo )
        print( f'{ separator }\nThe winner is { winner } width a bid of ${ bidders[ winner ]}!\n{ separator }' )

        input('\nPress ENTER to bid again\n')
        bidders = {}
        askBid()

def getWinner():
    return max( bidders )

askBid()