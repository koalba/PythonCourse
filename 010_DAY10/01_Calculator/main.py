import os
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    'x' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

result = 0

def start():
    result = 0

    printCalculator()
    operation = input('    ( E.g. 2 + 1, 2.1 * 10, ... )\n    Type your operation with spaces: \n    ')

    getNumbers( operation )

def calculate( first_number, operation , second_number ):
    result = ops[ operation ]( first_number , second_number )
    return round( result ) if result.is_integer( ) else round( result , 2 )

def getNumbers( string ):
    global result 
    numbers = string.split(' ')
    
    while len(numbers) > 1:
        for i, n in enumerate( numbers ):
            if n == '*' or n == '/' or n == '%' or n == '^' or n == 'x':
                numbers[i] = calculate( float(numbers[i - 1]), n , float(numbers[i + 1]) )
                numbers.pop( i + 1 )
                numbers.pop( i - 1 )
        else:
            for i, n in enumerate( numbers ):
                if n == '+' or n == '-':
                    numbers[i] = calculate( float(numbers[i - 1]), n , float(numbers[i + 1]) )
                    numbers.pop( i + 1 )
                    numbers.pop( i - 1 )

    result = numbers[0]
    printCalculator(f'{ string } = { result }')

def printCalculator( operation = '' ): #25
    calculator = f"""
     _____________________________________________________
    |  _________________________________________________  |
    | |                                                 | |
    | |{''.ljust( 48 - len(operation) if operation else 47, ' ' ) }{ operation if operation else '0' } | |
    | |_________________________________________________| |
    |  ___________ ___________ ___________   ___________  |
    | |           |           |           | |           | |
    | |     7     |     8     |     9     | |     +     | |
    | |___________|___________|___________| |___________| |
    | |           |           |           | |           | |
    | |     4     |     5     |     6     | |     -     | |
    | |___________|___________|___________| |___________| |
    | |           |           |           | |           | |
    | |     1     |     2     |     3     | |     x     | |
    | |___________|___________|___________| |___________| |
    | |           |           |           | |           | |
    | |     .     |     0     |     =     | |     /     | |
    | |___________|___________|___________| |___________| |
    |_____________________________________________________|
"""
    os.system('clear')
    print( calculator )

    if operation:
        response = input( f"    Press 'c' to continue calculating with { result }.\n    Press 'n' to start a new calculation.\n    " ).lower()
        if response == 'c':
            os.system('clear')
            print( calculator )
            op = str( result ) + ' ' + input(f'    Type your operation with spaces: \n    { result } ')
            getNumbers( op )
        else:
            start()

start()