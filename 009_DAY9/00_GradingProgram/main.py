grades = {
    'Fail'                 : ( 0  , 70  ), 
    'Acceptable'           : ( 71 , 80  ), 
    'Exceeds Expectations' : ( 81 , 90  ), 
    'Outstanding'          : ( 91 , 100 )
}
    
student_scores = {
    'Alba'   : 85,
    'Dani'   : 97,
    'Pablo'  : 50,
    'Lorena' : 100,
    'Pedro'  : 75
}

def convertGrades( list ):
    student_grades = {}

    for key in list:
        for grade in grades:
            if list[ key ] >= grades[ grade ][0] and list[ key ] <= grades[ grade ][1]:
                student_grades[ key ] = grade

    return student_grades


print( convertGrades( student_scores ) )