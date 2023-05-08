from turtle import Turtle
import random

class Ball(Turtle):

    def __init__( self ):
        super().__init__()

        self.shape('circle')
        self.color('white')
        self.penup()

        self.reset()

        self.move_speed = .005

    def move( self ):
        new_x = self.xcor() + 1 * self.dir_x
        new_y = self.ycor() + 1 * self.dir_y
        self.goto( new_x , new_y )

        self.detect_wall_collision()

    def detect_wall_collision( self ):
        if self.ycor() >= 233 or self.ycor() <= -230:
            self.dir_y *= -1

    def detect_paddle_collision( self , paddle : Turtle ):
        if paddle.xcor() < 0:
            check_xcor = self.xcor() < paddle.xcor() + 20
            check_xcor2 = self.xcor() < paddle.xcor() + 10 and self.xcor() > paddle.xcor() - 20
            check_xcor3 = self.xcor() < paddle.xcor() + 20
        else:
            check_xcor = self.xcor() > paddle.xcor() - 20
            check_xcor2 = self.xcor() > paddle.xcor() - 10 and self.xcor() < paddle.xcor() + 20
            check_xcor3 = self.xcor() > paddle.xcor() - 20

        if check_xcor and self.ycor() < paddle.ycor() + 50 and self.ycor() > paddle.ycor() - 50:
            self.dir_x *= -1
            self.move_speed *= .9

        elif check_xcor2 and self.ycor() < paddle.ycor() + 60 and self.ycor() > paddle.ycor() - 60:
            self.dir_y *= -1
            self.move_speed *= .9

        elif check_xcor3 and self.ycor() < paddle.ycor() + 60 and self.ycor() > paddle.ycor() - 60:
            self.dir_x *= -1
            self.dir_y *= -1
            self.move_speed *= .9

    def reset( self ):
        self.goto( 0 , 0 )
        self.dir_x = random.choice([-1 , 1])
        self.dir_y = random.choice([-1 , 1])
        self.move_speed = .005
