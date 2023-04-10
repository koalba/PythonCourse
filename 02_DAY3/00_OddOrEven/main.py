def question():
    try:
        number = int( input('Write a number: ') )
        num_type = 'EVEN' if isItEven(number) else 'ODD'
        print(f'{number} is an {num_type} number')
    except ValueError:
        print( 'Invalid number, try again' )
        question()

def isItEven( n ):
    return n % 2 == 0
    
question()