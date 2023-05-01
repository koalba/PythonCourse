from turtle import Turtle, Screen
import random

WIDTH, HEIGHT       = 500 , 500

tim = Turtle()
tim.shape('turtle')
tim.color('yellowgreen')

for _ in range(25):
    tim.fd( 5 )
    if tim.isdown() : tim.penup()
    else : tim.pendown()

screen = Screen()
screen.bgcolor('#22272e')
screen.setup( WIDTH , HEIGHT )
screen.exitonclick()