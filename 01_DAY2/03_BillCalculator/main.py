def questionaire():
    try:
        total_bill = float( input('What was de total bill? $') )
        tip_percentage = float( input('What percentage tip would you like to give?') )
        people = int( input('How many people to split the bill?') )

        print( 'Each person should pay: ${}'.format( calculateTip( total_bill , tip_percentage , people )))
    except ValueError:
        print('That value was invalid, try again')
        questionaire()

def calculateTip( bill , percentage , people ):
    tip = ( percentage * bill ) / 100
    total_person = ( bill + tip ) / people
    return round( total_person , 2 )

questionaire()