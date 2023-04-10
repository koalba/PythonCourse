# def add( number ):
#     return int(number[0]) + int(number[1])

def add( num ):
    sum = 0
    for n in num:
        sum += int(n)
    return sum

def question():
    number = input('Type a more than two digit number: ')
    if number.isnumeric() and int(number) > 10:
        print( add( list(number) ) )
    else: 
        print('That is not a more than two two digit number, try again')
        question()

question()

