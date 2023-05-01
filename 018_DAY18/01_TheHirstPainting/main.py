from turtle import Turtle, Screen
import colorgram
import random

NUM           = 10
WIDTH, HEIGHT = 500 , 500
DOT_SIZE      = 15
SPACING       = ( WIDTH - DOT_SIZE) / NUM

colors = colorgram.extract('image.webp', 20)
PALLETE = [ color.rgb for color in colors if color.proportion < 0.03 ]

screen = Screen()
screen.colormode(255)
screen.setup( WIDTH , HEIGHT )

tim = Turtle()
tim.shape('turtle')
tim.color('yellowgreen')
tim.hideturtle() 
tim.penup()

up = 0
position = ( WIDTH / 2 - DOT_SIZE * 2 ) * -1

for x in range( 10 ):
    tim.goto( position  , position + up )
    for _ in range( NUM ):
        tim.dot( DOT_SIZE , random.choice( PALLETE ) )
        tim.forward( SPACING )
    up += SPACING

screen.tracer(0)
screen.exitonclick()