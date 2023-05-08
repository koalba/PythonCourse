from turtle import Turtle

class Scoreboard(Turtle):
    score = 0
    best_score = 0

    def __init__( self ):
        super().__init__()

        self.hideturtle()
        self.goto( 0 , 265 )
        self.pencolor('white')

        self.update_score()

    def increase_score( self ):
        self.score += 1
        self.update_score()

    def update_score( self ):
        self.clear()
        self.write(f'Score: { self.score }', False , 'center', ('Courier', 16 , 'normal'))

    def game_over( self ):
        if self.score > self.best_score:
            self.best_score = self.score

        self.goto( 0 , 30 )
        self.write('GAME OVER', False , 'center', ('Courier', 24 , 'normal'))

        self.goto( 0 , 0 )
        self.write('- Press ENTER to play again -', False , 'center', ('Courier', 16 , 'normal'))

        self.goto( 0 , -60 )
        self.write(f'Best Score: { self.best_score }', False , 'center', ('Courier', 16 , 'normal'))

        self.goto( 0 , -270 )
        self.write('- Press ESC to exit -', False , 'center', ('Courier', 16 , 'normal'))

    def reset_scoreboard( self ):
        self.goto( 0 , 265 )
        self.score = 0
        self.update_score()
