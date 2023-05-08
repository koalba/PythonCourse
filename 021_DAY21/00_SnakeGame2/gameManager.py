from turtle import Turtle, Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

SCREEN_SIZE  = 600

class GameManager(Turtle):
    game_is_on = False

    screen     : Screen
    snake      : Snake
    food       : Food 
    scoreboard : Scoreboard

    def __init__( self ) -> None:
        super().__init__()
        self.hideturtle()
        self.pencolor('white')

        self.setup_screen()
        self.main_menu()

        self.screen.exitonclick()

    def main_menu( self ):
        self.goto( 0 , 30 )
        self.write('My Snake Game', False , 'center', ('Courier', 24, 'normal'))
        
        self.goto( 0 , 0 )
        self.write('- Press ENTER to start the game -', False , 'center', ('Courier', 16 , 'normal'))

        self.goto( 0 , -270 )
        self.write('- Press ESC to exit -', False , 'center', ('Courier', 16 , 'normal'))

        self.screen.listen()
        self.screen.onkey( self.start_game, 'Return')
        self.screen.onkey( quit, 'Escape')

    def setup_screen( self ) -> None:
        self.screen = Screen()

        self.screen.setup  ( SCREEN_SIZE , SCREEN_SIZE )
        self.screen.bgcolor('black')
        self.screen.title  ('My Snake Game')
        self.screen.tracer ( 0 )

    def listen_events( self ) -> None:
        self.screen.listen()
        self.screen.onkey( self.snake.up    , 'Up'   )
        self.screen.onkey( self.snake.down  , 'Down' )
        self.screen.onkey( self.snake.left  , 'Left' )
        self.screen.onkey( self.snake.right , 'Right')

    def start_game( self ) -> None:
    
        try:
            self.snake
        except AttributeError:
            self.snake      : Snake      = Snake()
            self.food       : Food       = Food()
            self.scoreboard : Scoreboard = Scoreboard()

        self.reset()
        self.listen_events()

        while self.game_is_on:
            time.sleep( .05 )
            self.snake.move()
            self.screen.update()

            self.detect_food_collision()
            self.detect_wall_collision()
            self.detect_self_collision()            

    def detect_food_collision( self ):
        # Detect collision with food
        if self.snake.head.distance( self.food ) < 15:
            self.food.refresh()
            self.snake.extend()
            self.scoreboard.increase_score()
    
    def detect_wall_collision( self ):
        # Detect collision with wall
        if self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290 or self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290:
            self.scoreboard.game_over()

            self.game_is_on = False
            self.game_over()

    def detect_self_collision( self ):
        # Detect collision with tail
        for segment in self.snake.snake_body[1:]:
            if self.snake.head.distance( segment ) < 5:
                self.scoreboard.game_over()
                self.game_is_on = False
                self.game_over()

    def game_over( self ) -> None:
        self.screen.listen()
        self.screen.onkey( self.start_game, 'Return')

    def reset( self ) -> None:
        self.screen.clear()
        self.screen.reset()

        self.setup_screen()

        self.scoreboard.reset_scoreboard()
        self.snake.reset_snake()
        self.food = Food()

        self.game_is_on = True
