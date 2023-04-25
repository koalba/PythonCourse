from question_model import Question
from art import logo, clear
from data import get_data

import requests
import json

class QuizBrain:

    def __init__ ( self ):
        self.q_list = []
        self.q_num  = 0
        self.score  = 0

    def still_has_questions( self ):
        return self.q_num < len( self.q_list )

    def next_question( self ):
        current = self.q_list[ self.q_num ]
        self.q_num += 1
        u_answer = input(f'    Q.{ self.q_num }: { current.text }\n    (True/False):\n    ').title()

        self.check_answer( u_answer , current.answer )

    def check_answer( self , u_answer : str , c_answer : str ):
        clear()

        if u_answer == c_answer:
            print('    You got it right!')
            self.score += 1
        else :
            print(f'    That\'s wrong! The correct answer was: { c_answer }.')
        print(f'    Your current score is: { self.score }/{ self.q_num }. You have { len( self.q_list ) - self.q_num } questions left.\n')

    def fill_quiz( self , difficulty : str ):
        question_data = get_data( difficulty )

        for question in question_data:
            q = Question( question['question'] , question['correct_answer'] )
            self.q_list.append( q )

