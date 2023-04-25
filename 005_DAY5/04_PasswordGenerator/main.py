import random
data = {}

data['letters'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
data['numbers'] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
data['symbols'] = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

data['nr_letters'] = int(input("How many letters would you like in your password?\n")) 
data['nr_symbols'] = int(input(f"How many symbols would you like?\n"))
data['nr_numbers'] = int(input(f"How many numbers would you like?\n"))

password = ''

def buildPassword():
    global password
    
    getRange( 'letters' )
    getRange( 'symbols' )
    getRange( 'numbers' )

    print( randomize( password ) )

def getRange( type ):
    global password
    for n in range( 0, data[ 'nr_' + type ] ):
        password += data[ type ][ n ]

def randomize( s ):
    # sample() is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set.
    return ''.join( random.sample( s, len( s ) ) )

buildPassword()
