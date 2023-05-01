from turtle import Turtle, Screen

WIDTH , HEIGHT = 500 , 500
SPEED = 5

s = Screen()
s.setup( WIDTH , HEIGHT )

t = Turtle()
t.speed('fastest')

def move_forward():
    t.fd( SPEED )

def move_backwards():
    t.bk( SPEED )

def rotate_left():
    t.lt( SPEED )

def rotate_right():
    t.rt( SPEED )

def clear():
    s.resetscreen()

s.onkey( move_forward   , 'w' )
s.onkey( move_backwards , 's' )
s.onkey( rotate_left    , 'a' )
s.onkey( rotate_right   , 'd' )
s.onkey( clear          , 'c' )

s.listen()
s.exitonclick()