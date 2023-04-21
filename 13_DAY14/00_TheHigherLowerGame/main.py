from art import logo
from game_data import data, text

import random
import os

os.system('clear')

def getRandomMatch():
    return random.choice( data )

def startGame():
    hasLost = False

    score = 0
    first_match  = getRandomMatch()
    second_match = getRandomMatch()

    while first_match['name'] == second_match['name']:
        second_match = getRandomMatch()

    while not hasLost:
        printBoard( first_match , second_match , score )
        answer = askUser()

        if   answer == 'A': itsCorrect = checkAnswer( first_match , second_match )
        elif answer == 'B': itsCorrect = checkAnswer( second_match , first_match )
        
        if not itsCorrect:
            hasLost = True
            continue
        else:
            score += 1
            first_match  = second_match
            second_match = getRandomMatch()

            while first_match['name'] == second_match['name']:
                second_match = getRandomMatch()

    else:
        os.system('clear')
        print( logo )
        print( f"\n   You choose: { first_match['name'] if answer == 'A' else second_match['name'] }." )
        print( f"   { first_match['name']  } : { first_match['follower_count'] } followers VS. { second_match['name'] } : { second_match['follower_count'] } followers." )
        print(f'\n   You scored: { score }')
        print( text[ str( score ) ]  if score <= 10 else text['10'] )


        input('\n   Press ENTER to play again\n   ')
        startGame()

def checkAnswer( one , two ):
    if one['follower_count'] > two['follower_count'] : 
        return True

    return False

def askUser():
    return input("\n   Who has more followers? Type 'A' or 'B': " ).upper()

def printBoard( fst , scnd , score ):
    os.system('clear')

    print( logo )
    if score : print( f"\n   You're right! Current Score: { score }" )
    print( f"\n   Compare A: { fst['name'] } a { fst['description'] } from { fst['country'] }" )
    print( f"   Against B: { scnd['name'] } a { scnd['description'] } from { scnd['country'] }" )


print( logo )
print('\n   Guess wich has more followers!')
input('   Press ENTER to start game\n   ')
startGame()