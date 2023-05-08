from turtle import Turtle

class Scoreboard(Turtle):
    scores = {
        'Player 1' : 0,
        'Player 2' : 0    
    }

    def __init__( self ):
        super().__init__()

        self.hideturtle()
        self.pencolor('white')
        self.penup()

        self.update_score()

    def increase_score( self , player ):
        self.scores[player] += 1
        self.update_score()

    def update_score( self ):
        self.clear()
        for i, player in enumerate( self.scores ):
            self.goto( -200 if i == 0 else 200 , 220 )
            self.write(f'{ player }: { self.scores[player] }', False , 'center', ('Courier', 16 , 'normal'))

