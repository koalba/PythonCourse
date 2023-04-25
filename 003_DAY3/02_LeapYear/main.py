def question():
    try:
        year = int( input('Which year do you want to check? ') )
        if isItLeapYear(year):
            print(f'{ year } is a leap year')
        else:
            print(f'{ year } is NOT a leap year')

    except ValueError:
        print('That is an invalid year, try again')
        question()

def isItLeapYear( year ):
    if( year % 4 == 0 and year % 100 != 0  or 
        year % 4 == 0 and ( year % 100 == 0 and year % 400 == 0 )):
        return True

    return False

question()
    