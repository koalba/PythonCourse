from turtle import Screen
from snake  import Snake
import time

SCREEN_SIZE  = 600

s = Screen()

s.setup  ( SCREEN_SIZE , SCREEN_SIZE )
s.bgcolor('black')
s.title  ('My Snake Game')
s.tracer ( 0 ) 

snake = Snake()

s.listen()
s.onkey( snake.up    , 'Up'   )
s.onkey( snake.down  , 'Down' )
s.onkey( snake.left  , 'Left' )
s.onkey( snake.right , 'Right')

game_is_on = True

while game_is_on:
    s.update()
    time.sleep(0.1)

    snake.move()

s.exitonclick()