def calculateBMI( h , w ):
    return int( w / ( h * h ) )

def questionaire():
    height = input('Enter your height in m: ')
    weight = input('Enter your weight in kg: ')

    try:
        print( calculateBMI( float(height) , float(weight) ) )
    except ValueError:
        print('One or both of the values are not correct, try again')
        questionaire()

questionaire()