from typing import Dict

class MenuItem: 
    
    def __init__( self , name : str , price : float , ingredients : Dict ) -> None:
        self.name        : str   = name
        self.price       : float = price
        self.ingredients : Dict  = ingredients

    def __str__( self ) -> None:
        return self.name

class Menu:
    menu_items : Dict = {}

    def __init__( self , items : Dict ) -> None:
        self.menu_items = { str(i) : i for i in items }

    def add_menu_item( self , item : MenuItem ) -> None:
        """Adds a new MenuItem to the menu.
        
        :item: The new MenuItem
        """
        self.menu_items[ str(item) ] = item
        
    def get_items( self ) -> str :
        """Returns all the names of the available menu items as a concatenated string."""
        return '/'.join( self.menu_items )
    
    def find_drink( self, order_name : str ) -> MenuItem :
        """Searches the menu for a particular drink by name. Returns a MenuItem object if it exists.

        :order_name: The name of the drinks order.
        """
        return self.menu_items[ order_name ]