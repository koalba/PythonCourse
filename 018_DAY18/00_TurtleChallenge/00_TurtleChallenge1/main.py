from turtle import Turtle, Screen
import random

WIDTH, HEIGHT       = 500 , 500

tim = Turtle()
tim.shape('turtle')
tim.color('yellowgreen')

for _ in range(4):
    tim.forward( 100 )
    tim.right( 90 )

screen = Screen()
screen.bgcolor('#22272e')
screen.setup( WIDTH , HEIGHT )
screen.exitonclick()