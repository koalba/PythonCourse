from turtle import Screen
import time

from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

SCREEN_WIDTH, SCREEN_HEIGHT = 800 , 500

s = Screen()
s.setup( SCREEN_WIDTH , SCREEN_HEIGHT )
s.bgcolor('black')
s.title  ('My Pong Game')
s.tracer ( 0 )

players = [
    {
        'name' : 'Player 1',
        'keyup' : 'Up',
        'keydown' : 'Down',
        'paddle' : Paddle(( 350, 0 )),
    },
    {
        'name' : 'Player 2',
        'keyup' : 'w',
        'keydown' : 's',
        'paddle' : Paddle(( -350, 0 )),
    }
]

ball = Ball()
scoreboard = Scoreboard()

s.listen()
for player in players:
    s.onkey( player['paddle'].up , player['keyup'] )
    s.onkey( player['paddle'].down , player['keydown'] )

game_is_on = True
while game_is_on:
    time.sleep( ball.move_speed )
    ball.move()
    s.update()

    for player in players:
        ball.detect_paddle_collision( player['paddle'] )

    if ball.xcor() > 390:
        scoreboard.increase_score( players[0]['name'] )
        ball.reset()
    elif ball.xcor() < -390:
        scoreboard.increase_score( players[1]['name'] )
        ball.reset()


s.exitonclick()