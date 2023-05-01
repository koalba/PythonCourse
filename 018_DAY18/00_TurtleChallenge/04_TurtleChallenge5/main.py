from turtle import Turtle, Screen, colormode
import random

WIDTH, HEIGHT       = 500 , 500
PEN_SIZE  = 2
LEN_CIRCLES = 100

colormode(255)

tim = Turtle()
tim.shape('turtle')
tim.color('yellowgreen')
tim.speed('fastest')

tim.hideturtle()
tim.pensize( PEN_SIZE )

for _ in range(100):
    
    r = random.randint(0, 250)
    g = random.randint(0, 250)
    b = 255

    tim.pencolor( r , g , b )

    tim.circle(LEN_CIRCLES)
    tim.rt( 360 / LEN_CIRCLES )

screen = Screen()
screen.bgcolor('#22272e')
screen.setup( WIDTH , HEIGHT )
screen.exitonclick()