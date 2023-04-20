from art import logo
import random
import os
os.system('clear')


answer = 0
finished = False

def getRandomNumber():
    return random.randint(0, 100)

def startGame( difficulty ):
    os.system('clear')

    global answer
    global finished

    answer = 0
    finished = False

    number = getRandomNumber()
    attempts = 10

    if difficulty == 'hard':
        attempts = 5

    while not finished :
        try:
            print( logo )

            if answer:
                if   answer > number : print('\n    Too High\n    Guess again.')
                elif answer < number : print('\n    Too Low\n    Guess again.' )
                else :
                    finished = True
                    continue

            print(f'\n    You have { attempts } attempts left.')
            answer = int( input( '    Make a guess: ' ) )

            os.system('clear')

            if not attempts == 0 : attempts -= 1
            if     attempts == 0 : finished = True
                

        except ValueError:
            os.system('clear')
            print('\n    That is not a valid guess. Please type a number.')
    
    else:
        os.system('clear')
        if answer == number:
            print( logo )
            print(f'\n    You got it! The answer was { number }.')
        elif attempts == 0:
            print( logo )
            print(f'\n    You\'ve run out of guesses, you lose.')

        difficulty = input('\n    Want to play again? Choose a difficulty. Type \'easy\' or \'hard\':\n    ').lower
        startGame( difficulty )

print( logo )
difficulty = input('\n    Choose a difficulty. Type \'easy\' or \'hard\':\n    ').lower()
startGame( difficulty )