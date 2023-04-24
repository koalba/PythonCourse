from typing import Dict

class CoffeeMaker():

    def __init__( self ) -> None :
        self.resources = {
            'water'  : 300,
            'coffee' : 100,
            'milk'   : 200
        }

    def report( self ) -> None :
        """ Prints a report of all resources """
        for r in self.resources:
            print( f"    { r.title() } : { self.resources[r] }{ 'gr' if r == 'coffee' else 'ml' }" )

    def manage_resources( self, ingredients : Dict ) -> bool :
        """ Returns True when the drink order can be made, False if ingredients are insufficient.
        
        :ingredients: (dict) The ingredients of the MenuItem to make.
        """
        for i in ingredients:
            if ingredients[i] > self.resources[i]:
                print(f'    Sorry there is not enough { i }.\n')
                return False
        return True
    
    def make_coffee( self , ingredients : Dict ) -> None :
        """Deducts the required ingredients from the resources.
        
        :ingredients: (dict) The ingredients of the MenuItem to make.
        """
        for i in ingredients:
            self.resources[i] -= ingredients[i]
