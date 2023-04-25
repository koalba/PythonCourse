from quiz_brain import QuizBrain
from art import logo, clear

def startGame():
    clear()

    quiz = QuizBrain()

    print('    Let\'s start!')
    difficulty = input('    What difficulty do you want? Easy, Medium or Hard\n    ').lower()
    if difficulty == 'easy' or difficulty == 'medium' or difficulty == 'hard':
        quiz.fill_quiz( difficulty )

        clear()

        while quiz.still_has_questions():
            quiz.next_question()

        clear()

        print('    You\'ve completed the quiz!')
        print(f'    Your final score was: { quiz.score }/{ quiz.q_num }\n')

        difficulty = input('    Press ENTER to try again\n    ').lower()
        startGame()
    else:
        startGame()

startGame()