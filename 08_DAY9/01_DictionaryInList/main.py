import os
from other import logo, strings

travel_log = {}

def addNewCountry( name , times_visited , cities_visited ):
    travel_log[ name ] = {
        'times_visited'  : times_visited,
        'cities_visited' : cities_visited
    }

addNewCountry( 'Canada'  , 1 , ['Toronto', 'Montreal', 'Quebec'])
addNewCountry( 'France'  , 2 , ['Paris'])
addNewCountry( 'Uruguay' , 1 , ['Montevideo'])
addNewCountry( 'Japan'   , 1 , ['Tokio', 'Kamakura'])
addNewCountry( 'Italy'   , 3 , ['Rome', 'Venice', 'Florence', 'Naples', 'Pisa', 'Pompeii'])

def checkTravelLog():
    print( strings['title'] )
    for country in travel_log:
        val = travel_log[ country ]
        print(f'\n    { country.upper() }')
        print(f'    You\'ve visited { country } { val["times_visited"] } times.')
        print(f'    You\'ve been to { ", ".join(val["cities_visited"][0:-1]) } and { val["cities_visited"][-1] }.\n')
        print( strings['separator'] )
    
    input( strings['enter'] )
    startTravelLog()

def checkCountry( searched_country ):
    
    if searched_country in travel_log:
        country = travel_log[ searched_country ]
        print(f'\n    { searched_country.upper() }')
        print(f'    You\'ve visited { searched_country.capitalize() } { country["times_visited"] } times.')

        if len( country["cities_visited"] ) > 1:
            string = f'{", ".join(country["cities_visited"][0:-1]) } and { country["cities_visited"][-1]}' 
        else:
            string = f'{ country["cities_visited"][0] }' 
        print(f'    You\'ve been to { string }.\n')

        print( strings['separator'] )

    else:
        print( strings['sorry'] )

    input( strings['enter'] )
    startTravelLog()

def startTravelLog():
    os.system('clear')

    print( logo )
    add_or_check = input( strings['menu'] ).capitalize()
    
    os.system('clear')

    if add_or_check == 'Modify':
        name = input( strings['country_name'] )
        times_visited = input( strings['times_visited'] )
        cities_visited = input( strings['cities'] ).replace(' ', '').split(',')

        addNewCountry( name , times_visited , cities_visited )

        os.system('clear')
        print( strings['added'] )
        checkCountry( name )

    elif add_or_check == 'Check': checkTravelLog()
    else : checkCountry( add_or_check )


startTravelLog()
