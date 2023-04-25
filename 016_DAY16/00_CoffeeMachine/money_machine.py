from typing import Dict
from art import clear

class MoneyMachine:
    values : Dict = {
        'penny'   : 0.01,
        'nickle'  : 0.05,
        'dime'    : 0.10,
        'quarter' : 0.25,
    }

    def __init__( self ) -> None :
        self.profit : float = 0

    def report( self ) -> None :
         """ Prints a report of the current profit """
         print( f"    Money : ${ self.profit }" )

    def ask_user_payment( self ) -> Dict :
        """ Asks the user for payment """
        clear()
        coins = {}
        
        print('    Please insert coins.\n')
        coins['quarter'] = int( input('    How many quarters? ') )
        coins['dime']    = int( input('    How many dimes? '   ) )
        coins['nickle']  = int( input('    How many nickles? ' ) )
        coins['penny']   = int( input('    How many pennies? ' ) )
        
        return coins

    def make_payment( self, cost : float ) -> bool :
        """ Returns True when payment is accepted, or False if insufficient.
         
        :cost: (float) The cost of the drink.
        """
        coins : Dict  = self.ask_user_payment()
        total : float = 0

        while total < cost:
            clear()

            for c in coins:
                total += coins[c] * self.values[c]
                
            if total < cost:
                print(f'    You have inserted: ${ total }.\n    Sorry that is not enough money, the cost is ${ cost }.\n')
                choice = input("    Do you want to 'insert' more or 'cancel' the transaction.\n    ").lower()

                if choice   == 'insert': coins = self.ask_user_payment()
                elif choice == 'cancel': return False

        else: 
            self.manage_money( total , cost )
            return True

    def manage_money( self , total : float , cost : float ):
        """Adds the cost of the drink to the machine profit and gives back the change.

        :total: (float) Total of the payment.

        :cost: (float) Cost of the drink.
        """
        self.profit += cost

        change : float = round(total - cost, 2)
        print( f"\n    Here is your ${ change } in change." ) if not total == cost else ''
        
        

    