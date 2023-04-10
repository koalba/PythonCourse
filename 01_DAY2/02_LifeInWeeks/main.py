def questionaire():
    age = input('What is your current age? ')
    
    try:
        int( age )
        print( calcLifeLeft( int(age) ) )
    except ValueError:
        print('That is not a valid answer, try again')
        age = input('What is your current age? ')

def calcLifeLeft( age ):
    years_left  = 90 - age
    
    days_left   = years_left * 365
    weeks_left  = years_left * 52
    months_left = years_left * 12

    return f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.'

questionaire()