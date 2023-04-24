from typing import Dict
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

from art import clear

default_menu_items : Dict = [
    MenuItem( 'espresso'  , 1.50 , { 'water' : 50 , 'coffee' : 18               } ),
    MenuItem( 'latte'     , 2.50 , { 'water' : 200, 'coffee' : 24, 'milk' : 100 } ),
    MenuItem( 'cappuccino', 3.00 , { 'water' : 250, 'coffee' : 24, 'milk' : 150 } ),
]    

menu           : Menu         = Menu( default_menu_items )
coffee_machine : CoffeeMaker  = CoffeeMaker()
money_machine  : MoneyMachine = MoneyMachine()

def startCoffeeMachine() -> None:
    " Whole Coffee Machine Proccess, from start to finish. "

    answer : str = input(f'    What would you like? ({ menu.get_items() }):\n    ').lower()

    if answer == 'report':
        clear()

        coffee_machine.report()
        money_machine .report()
        print('')

        startCoffeeMachine()

    elif answer == 'end':
        clear()
        end = input("    Are you sure yo want to turn off the machine?\n    Type 'Y' or 'N'.\n    ").lower()    
        if end == 'y':
            clear()
            print('    Have a nice day!\n')
            exit()

    try:
        product : MenuItem = menu.find_drink( answer )

        if coffee_machine.manage_resources( product.ingredients ):
            clear()
            if money_machine.make_payment( product.price ):

                coffee_machine.make_coffee( product.ingredients )
                print(f'    Here is your { str( product ).title() } ☕ Enjoy!\n')

                startCoffeeMachine()

            else: clear()

        startCoffeeMachine()
    
    except KeyError:
        clear()
        startCoffeeMachine()

clear()
startCoffeeMachine()