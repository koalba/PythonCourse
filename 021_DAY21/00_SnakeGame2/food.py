from turtle import Turtle
import random

FOOD = [
    {
        'color' : 'orange',
        'shape' : 'triangle'
    },
    {
        'color' : 'purple',
        'shape' : 'circle'
    }
]

class Food(Turtle):
    def __init__( self ):
        super().__init__()

        self.shapesize( 0.5 , 0.5 )
        self.speed('fastest')
        self.penup()

        self.refresh()


    def refresh( self ):
        food_type  = random.choice( FOOD )
        
        self.shape( food_type['shape'] )
        self.color( food_type['color'] )

        x_cor = random.randint( -275 , 275 )
        y_cor = random.randint( -275 , 275 )
        
        self.goto( x_cor , y_cor )

