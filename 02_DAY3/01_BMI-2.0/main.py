def calculateBMI( h , w ):
    return int( w / ( h ** 2 ))

def getInterpretation( val ):
    str = ''

    if val < 18.5:
        type = 'Slightly' if val > 13 else 'Severely'
        str = f'you are {type} underweight'
    elif val >= 18.5 and val < 25:
        str = 'you have normal weight'
    elif val >= 25 and val < 30:
        type = 'Slightly' if val > 27.5 else 'Severely'
        str = f'you are {type} overweight'
    elif val >= 30 and val < 35:
        type = 'Slightly' if val > 32.5 else 'Severely'
        str = f'you are {type} obese'
    else: 
        str = 'you are clinically obese'

    return str

def questionaire():
    height = input('Enter your height in m: ')
    weight = input('Enter your weight in kg: ')

    try:
        result = calculateBMI( float(height) , float(weight) )
        print( f'Your BMI is {result}, { getInterpretation(result) }' )
    except ValueError:
        print('One or both of the values are not correct, try again')
        questionaire()

questionaire()