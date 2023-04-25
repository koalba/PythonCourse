import random
import os

x = '❌'
n = '⬛'

def randomTreasure():
    row = random.randint(0, 2)
    column = random.randint(0, 2)

    map[row][column] = x

def askUser():
    global count

    res = input('Where is the Treasure Chest?\nType a coordinate to dig ( E.g. 12 )\n')

    row    = int( res[0] ) - 1
    column = int( res[1] ) - 1

    try:
        _ = res[1]
        map[ row ][ column ]
    except:
        startGame()

    if map[row][column] == x :
        clear_map[row][column] = x

        printMap()

        print('🪙  YOU FOUND THE CHEST! 🪙')
        input('\nPress ENTER to play again')

        reset()
        startGame()
    else:
        clear_map[row][column] = n
        count = count - 1

        printMap()

        if count:
            askUser()
        else:
            print("GAME OVER! You've run out of attempts...")
            input('\nPress ENTER to play again')

            reset()
            startGame()


def printMap():
    os.system('clear')
    print( f"\nYou've { count } attempts left\n" )
    print(f'      1     2     3   \n\n1   { clear_row1 }\n\n2   { clear_row2 }\n\n3   { clear_row3 }\n')

def startGame():
    randomTreasure()
    printMap()
    askUser()

def reset():
    global count, clear_row1, clear_row2, clear_row3, clear_map, row1, row2, row3, map

    count = 4

    clear_row1 = ['⬜', '⬜', '⬜']
    clear_row2 = ['⬜', '⬜', '⬜']
    clear_row3 = ['⬜', '⬜', '⬜']

    clear_map = [ clear_row1, clear_row2, clear_row3 ]

    row1 = ['⬜', '⬜', '⬜']
    row2 = ['⬜', '⬜', '⬜']
    row3 = ['⬜', '⬜', '⬜']

    map = [ row1, row2, row3 ]

reset()
startGame()
