from turtle import Turtle

RIGHT = 0
UP    = 90
LEFT  = 180
DOWN  = 270

START_BODY_LENGTH : int = 3
SEGMENT_SIZE      : int = 20
SPEED             : int = 20

class Snake:
    snake_body = []

    def __init__( self ):
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake( self ):
        for i in range( START_BODY_LENGTH ):
            segment = Turtle('square')

            segment.penup()
            segment.color('white')
            segment.setx( - SEGMENT_SIZE * i )

            self.snake_body.append(segment)

    def move( self ):
        for num in range( len( self.snake_body ) - 1 , 0 , -1 ):
            x_cor = self.snake_body[ num - 1 ].xcor()
            y_cor = self.snake_body[ num - 1 ].ycor()

            self.snake_body[ num ].goto( x_cor , y_cor )

        self.head.forward( SPEED )

    def up( self ):
        if self.head.heading() != DOWN:
            self.head.setheading( UP )

    def down( self ):
        if self.head.heading() != UP:
            self.head.setheading( DOWN )

    def left( self ):
        if self.head.heading() != RIGHT:
            self.head.setheading( LEFT )

    def right( self ):
        if self.head.heading() != LEFT:
            self.head.setheading( RIGHT )