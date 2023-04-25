pizza_prize = {
    'S' : {
        'price' : 15,
        'extra_pepperoni' : 2,
        'extra_cheese' : 1
    },
    'M' : {
        'price' : 20,
        'extra_pepperoni' : 3,
        'extra_cheese' : 1
    },
    'L' : {
        'price' : 25,
        'extra_pepperoni' : 3,
        'extra_cheese' : 1
    },
}

pizza_names = {
    'S' : 'Small',
    'M' : 'Medium',
    'L' : 'Large'
}

def getOrder():
    print('Welcome to Python Pizza Deliveries!')
    size = ''
    pepperoni = ''
    extra_cheese = ''

    while size != 'S' and size != 'M' and size != 'L':
        if size:
            print('That is not a valid pizza size, choose between S, M or L')
        size = input('What size pizza do you want? S, M or L?\n').upper()

    while pepperoni != 'Y' and pepperoni != 'N':
        if pepperoni:
            print('That is not a valid answer, choose between Y or N')
        pepperoni = input('Do you want pepperoni? Y or N\n').upper()

    while extra_cheese != 'Y' and extra_cheese != 'N':
        if extra_cheese:
            print('That is not a valid answer, choose between Y or N')
        extra_cheese = input('Do you want extra cheese? Y or N\n').upper()

    calcBill( size , pepperoni , extra_cheese )

def calcBill( size, pepperoni, cheese ):

    price = pizza_prize[size]['price']
    pepperoni_price = pizza_prize[ size]['extra_pepperoni']
    cheese_price = pizza_prize[ size]['extra_cheese']

    bill =  price
    bill += pepperoni_price if pepperoni == 'Y' else 0
    bill += cheese_price    if cheese    == 'Y' else 0

    print(f"- { pizza_names[ size ] } Pizza: ${ price }")
    if pepperoni == 'Y':
        print(f'- Extra Pepperoni: +${ pepperoni_price }')
    if cheese == 'Y':
        print(f'- Extra Cheese: +${ cheese_price }')
    print(f'TOTAL: ${bill}')


getOrder()