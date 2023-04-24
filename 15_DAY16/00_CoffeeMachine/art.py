machine = '''
     _____________________ _____
    |  _________________  | ___ ||   ______________________
    | | ___/     \__/\  | | ___ ||  |                      ||
    | |/_______________\| |     ||  | PRICE CHART:         ||
    |                     |  _  ||  |                      ||
    |   O || Espresso     | |_| ||  | Espresso   -> $ 1.50 ||
    |   O || Latte        |     ||  | Latte      -> $ 2.50 ||
    |   O || Capuccino    |  -o ||  | Cappuccino -> $ 3.00 ||
    |    _____________    |     ||  |______________________||
    |   Y    |___|    Y   |     ||   
    |   |   |     |   |   |     ||
    |  ||    \___/    ||  | ___ ||
    |   0_____________0   | ___ ||
    |_  _______________  _|_ _ _||
'''

import os

def clear():
    """ Clears the screen and adds the Coffee Machine ASCII """
    os.system('clear')
    print( machine )


    



