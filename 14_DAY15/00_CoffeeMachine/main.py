from machine_data import MENU, COINS
from art import machine
import os
os.system('clear')

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}

total = 0

def processResources( ingredients ):
    for i in ingredients:
        if ingredients[i] > resources[i]:
            clear()
            print(f'    Sorry there is not enough { i }.\n')
            return False
    return True

def processCoins( coins , cost ):
    global total
    total = 0

    while total < cost:
        clear()

        for c in coins:
            total += coins[c] * COINS[c]
            
        if total < cost:
            print(f'    You have inserted: ${ total }.\n    Sorry that is not enough money, the cost is ${ cost }.\n')
            choice = input("    Do you want to 'insert' more or 'cancel' the transaction.\n    ").lower()

            if choice   == 'insert': coins = inputMoney()
            elif choice == 'cancel': return False

    else: return True

def makeCoffee( ingredients ):
    for i in ingredients:
        resources[i] -= ingredients[i]

def printReport():
    clear()
    for r in resources:
        if not r == 'money':
            print( f"    { r.title() } : { resources[r] }{ 'gr' if r == 'coffee' else 'ml' }" )
        else:
            print( f"    { r.title() } : ${ resources[r] }" )

    print('')

def clear():
    os.system('clear')
    print( machine )

def inputMoney():
    coins = {}
    clear()
    
    print('    Please insert coins.\n')
    coins['quarter'] = int( input('    How many quarters? ') )
    coins['dime']    = int( input('    How many dimes? '   ) )
    coins['nickle']  = int( input('    How many nickles? ' ) )
    coins['penny']   = int( input('    How many pennies? ' ) )
    
    return coins

def startCoffeeMachine():
    global total

    coins = {}
    answer = input('    What would you like? (espresso/latte/cappuccino):\n    ').lower()

    if answer == 'report':
        printReport()
        startCoffeeMachine()

    elif answer == 'end':
        clear()
        end = input("    Are you sure yo want to turn off the machine? Type 'Y' or 'N'. ").lower()    
        if end == 'y':
            clear()
            print('    Have a nice day!')
            return

    try:
        product = MENU[ answer ]

        if processResources( product['ingredients'] ):
            coins = inputMoney()

            if processCoins( coins , product['cost'] ):
                clear()

                resources['money'] += product['cost']
                print( f"\n    Here is your ${ round(total - product['cost'], 2) } in change." ) if not total == product['cost'] else ''

                makeCoffee( product['ingredients'] )
                print(f'    Here is your { answer.title() } ☕ Enjoy!\n')

                startCoffeeMachine()

            else: clear()

        startCoffeeMachine()
    
    except KeyError:
        clear()
        startCoffeeMachine()

print( machine )
startCoffeeMachine()