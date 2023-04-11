student_heights = [ 180 , 124 , 165 , 173 , 189 , 169 , 146 ]

def getAverage():
    average = sum( student_heights ) / len( student_heights )
    return round( average )

print( getAverage() )