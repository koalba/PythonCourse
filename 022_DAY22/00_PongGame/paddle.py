from turtle import Turtle

SPEED = 20

class Paddle(Turtle):
    def __init__( self , coor ) -> None:
        super().__init__()

        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize( 1 , 5 ) # 20 x 100

        self.setheading(90)
        self.goto( coor )

    def up( self ):
        if self.ycor() + 50 < 250:
            self.forward( SPEED )

    def down( self ):
        if self.ycor() - 50 > -250:
            self.backward( SPEED )
