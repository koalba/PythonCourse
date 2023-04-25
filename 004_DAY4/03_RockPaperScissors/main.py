import os
import random
from ascii import ascii_list as A

game_text = [
    " --------------- IT'S A DRAW ----------------",
    ' ----------- GAME OVER, YOU LOST! -----------',
    ' -------- CONGRATULATIONS, YOU WON! ---------' 
]

game_ascii = [
    [ 0, 1, 2 ],
    [ 3, 4, 5 ],
    [ 6, 7, 8 ],
]

game_choices = [
    [ 0, 1, 2 ], # Rock ------ 0
    [ 2, 0, 1 ], # Paper ----- 1
    [ 1, 2, 0 ]  # Scissors -- 2
]

def getChoices():
    os.system('clear')

    user_choice     = int( input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ') )
    computer_choice = random.randint(0, 2)

    try:
        print('\n --------------------------------------------')
        print(' - YOUR CHOICE ------------ COMPUTER CHOICE -')
        print(' --------------------------------------------')
        print(f'{ A[ game_ascii[ user_choice ][ computer_choice ] ] }')
        print(' --------------------------------------------')
        print( game_text[ game_choices[ user_choice ][ computer_choice ] ] )
        print(' --------------------------------------------')

        input('\n       - Press ENTER to play again -     \n')
        getChoices()
    except:
        os.system('clear')
        getChoices()

getChoices()