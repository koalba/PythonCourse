from turtle import Turtle, Screen, colormode
import random

WIDTH, HEIGHT       = 500 , 500
DEFAULT_SIDE_LENGTH = 100
MAX_SIDES           = 10

colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.color('yellowgreen')

for num in range( 3, MAX_SIDES + 1 ):
    tim.pencolor( tuple( random.choices(range(256), k=3) ) )

    for _ in range( num ):
        tim.fd( DEFAULT_SIDE_LENGTH )
        tim.rt( 360 / num )

screen = Screen()
screen.bgcolor('#22272e')
screen.setup( WIDTH , HEIGHT )
screen.exitonclick()