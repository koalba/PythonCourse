score_list = [ 78 , 65 , 89 , 86 , 55 , 91 , 64 , 89 ]

def getHighest( list ):
    largest = 0

    for x in list:
        if x > largest:
            largest = x

    return largest

print(f'The highest score in the class is: { getHighest( score_list ) }')