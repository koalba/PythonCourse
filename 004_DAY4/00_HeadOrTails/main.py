import random

def tossCoin():
    num = random.randint(0,1)
    return '    Heads\n' if num else '    Tails\n'

def ask():
    input('Press ENTER to toss coin\n')
    print( tossCoin() )

    ask()

ask()
