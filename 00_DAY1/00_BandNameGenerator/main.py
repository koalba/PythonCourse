def questionary():
    city = input("What's the name of the city you grew up in?\n")
    pet  = input("What's yout pet's name?\n")
    
    print( generateBandName( city , pet ) )

def generateBandName( city , pet ):
    return f'Your band could be { city } { pet }'
    return 'Your band could be {} {}'.format( city , pet )
    return 'Your band could be ' + ' '.join([ city , pet ])

questionary()