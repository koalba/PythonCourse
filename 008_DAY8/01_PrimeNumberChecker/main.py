answers = {
    'it_is'     : 'It\'s a prime number.',
    'it_is_not' : 'It\'s NOT a prime number.'
}

def isItPrime( num ):
    for n in range(2, num):
        if num % n == 0 :
            return answers['it_is_not']
    else:
        return answers['it_is']

def askUser():
    number = int( input('\nCheck this number: ') )
    if number <=1 :
        print( f'{ number } : { answers["it_is_not"] }')
    else:
        print( f'{ number } : { isItPrime( number ) }')
    askUser()

askUser()