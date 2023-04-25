import os
import random

from word_list import word_list
from hangman_ascii import hangman
from hangman_ascii import logo

board = []
user_lifes = 6

def getRandomWord():
    num = random.randint(0, len( word_list ) - 1)
    return word_list[num]

def startGame():
    global user_lifes
    game_over = False
    user_lifes = 6
    guess = []

    incorrect = False

    word = getRandomWord()

    global board
    board = ['_'] * len( word )

    while user_lifes and not game_over:

        printBoard( word , guess )

        letter = userGuess( incorrect )
        if not letter or ' ' in letter or len(letter) > 1 or letter.isdigit():
            incorrect = True
            continue

        incorrect = False

        guess.append( letter )

        if checkWord( word , letter ):
            game_over = True
            print('inside')
    else:
        if game_over:
            printBoard( word , guess )

            print('\n   Congratulations, YOU WON!')
            input('\n   Press ENTER to play again!\n   ')

            startGame()
        else:
            printBoard( word , guess )

            print(f'\n   YOU LOST... The word was { word }')
            input('\n   Press ENTER to play again!\n   ')

            startGame()

def printBoard( word , guess ):
    global user_lifes
    global board

    os.system('clear')
    
    print( f'\n   { hangman[ (user_lifes + 1) * -1 ]}' )
    print( f'   Used letters: { ", ".join( guess ).upper() }' )
    print( f'   Lifes: { user_lifes } ❤\n\n' )
    print( f'   { board }' )
    print(f'\n\n   The word has { len( word ) } letters.')
    

def userGuess( incorrect , letter = ''):
    if incorrect:
        question = f'\n   That wasn\'t a valid letter. Please choose Again:\n   '
    else:
        question = '\n   Choose a letter:\n   '
    
    return input( question ).lower()

def checkWord( word , letter ):
    global user_lifes
    global board

    try:
        word.index( letter )

        for i, l in enumerate( word ):
            if l == letter:
                board[i] = letter.upper()

        if ''.join( board ).lower() == word:
            return True

    except ValueError:
        user_lifes -= 1

    return False
        
def menu():
    os.system('clear')
    print(f'   { logo }')
    print('\n\n   Try to guess the word without getting hanged!')
    print('   Practice your spelling and word-decoding skills with this game.')
    input('\n   Press ENTER to play!\n   ')
    startGame()

menu()
    