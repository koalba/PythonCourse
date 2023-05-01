from turtle import Turtle, Screen
import random

WIDTH , HEIGHT = 500 , 500

s = Screen()
s.setup( WIDTH , HEIGHT )

is_race_on = False

color_list  = [ 'red', 'orange', 'gold', 'green', 'blue', 'violet' ]
y_positions = [ -70, -40, -10, 20, 50, 80 ]
turtle_list = []

user_bet = s.textinput( title = 'Make your bet' , prompt = f'Which Turtle will win the race?\n({", ".join(color_list)})\n\nEnter a color :')

for n in range(6):
    t = Turtle( shape='turtle' )
    t.color( color_list[n] )
    t.penup()
    t.goto( ( WIDTH / 2 - 20 ) * -1 , y_positions[n] )
    turtle_list.append( t )

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtle_list:
        rand_distance = random.randint(0, 10)
        t.forward( rand_distance )

        if t.xcor() > WIDTH / 2 - 20 :
            if user_bet == t.pencolor():
                print(f'You won! The { t.pencolor() } turtle won the race!')
            else:
                print(f'You lost! The { t.pencolor() } turtle is the winner.')
            is_race_on = False

s.exitonclick()