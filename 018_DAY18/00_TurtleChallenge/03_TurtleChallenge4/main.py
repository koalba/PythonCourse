from turtle import Turtle, Screen, colormode
import random

WIDTH, HEIGHT = 500 , 500
PEN_SIZE  = 2

colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.color('yellowgreen')
tim.speed('fastest')

tim.hideturtle()
tim.pensize( PEN_SIZE )

while True:

    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = 255

    tim.pencolor( r , g , b )
    tim.fd( 10 )

    tim.rt( random.choice([ 0, 90, 180, 270, 360 ]) )

screen = Screen()
screen.bgcolor('#22272e')
screen.setup( WIDTH , HEIGHT )
screen.exitonclick()