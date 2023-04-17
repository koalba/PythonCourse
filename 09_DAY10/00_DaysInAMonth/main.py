import os
month_text = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def question():
    try:
        year = int( input('Enter a year: ') )
    except ValueError:
        os.system('clear')
        print('That is an invalid year, try again')
        question()

    try: 
        month = int( input('Enter a month (number): ') )
        if month > 12 or month <= 0:
            raise ValueError
    except ValueError:
        os.system('clear')
        print('That is an invalid month, try again')
        question()

    print( f'\nThere is { days_in_month( year , month ) } days in { month_text[ month - 1 ] }, { year }.\n' )

def isItLeapYear( year ):
    if( year % 4 == 0 and year % 100 != 0  or 
        year % 4 == 0 and ( year % 100 == 0 and year % 400 == 0 )):
        return True

    return False

def days_in_month( year , month ):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isItLeapYear( year ) and month == 2:
        return 29
    else:
        return month_days[ month - 1 ]
    
os.system('clear')
question()
    