import os
from ascii import allAscii as _

class Choice:
    user_choice = ''

    def __init__( self , text , choices ):
        self.text = text
        self.choices = choices

    def __str__(self):
        return self.text

    def filterChoices( self, value ):
        while not value in self.choices:
            os.system('clear')
            value = input( self ).lower()
        else:
            os.system('clear')
            self.user_choice = value
            return self.choices[ self.user_choice ]
                
      
game_choices = [
    Choice(
        f'{ _["crossroad_ascii"] }You\'re at a cross road. Where do you want to go? Type "left" or "right"\n',
        {
            'left' : { 'value' : True },
            'right' : {
                'value' : False,
                'text'  : f'{ _["hole_ascii"] }You fell into a hole. GAME OVER\n'
            }
        }
    ),
    Choice(
        f'{ _["lake_ascii"] }You come to a lake with an island in the middle.\nType "wait" to wait for a boat. Type "swim" to swim across.\n',
        {
            'wait' : { 'value' : True },
            'swim' : {
                'value' : False,
                'text'  : f'{ _["fish_ascii"] }You got attacked by an angry Trout. GAME OVER\n'
            }
        }
    ),
    Choice(
        f'{ _["door_ascii"] }You arrive at the island unharmed, there is a house with 3 doors. One red, one yellow and one blue.\nWhich color do you choose?\n',
        {
            'yellow' : { 'value' : True },
            'red' : {
                'value' : False,
                'text'  : f'{ _["fire_ascii"] }It\'s a room full of fire. GAME OVER\n'
            },
            'blue' : {
                'value' : False,
                'text'  : f'{ _["monster_ascii"] }You enter a room of beasts. GAME OVER\n'
            }
            
        }
    )
]

def startGame():
    for c in game_choices:
        result = c.filterChoices( input( c ).lower() )

        if result['value'] :
            continue
        else:
            ready( True , result['text'] )
            return
    else:
        text = f'{ _["treasure_ascii"] }Congratulations, you found the treasure!\n'
        ready( True, text )

def ready( restart, text = '' ):
    os.system('clear')
    if( restart ):
        print(text)
        start = input('Want to start again? Type START\n').lower()
    else:
        print(f'{ _["island_ascii"] }Welcome to Treasure Island!\nYour mission is to find the hidden treasure.\n')
        start = input('Type START to play\n').lower()

    if start == 'start' :
        os.system('clear')
        startGame()
    else:
        ready( restart , text )

ready( False )