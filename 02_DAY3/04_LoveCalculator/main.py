def loveCalculator():
    user_name  = input('What is your name? ' )
    crush_name = input('What is their name? ')

    true_matches = len([ x for x in user_name.lower() + crush_name.lower() if x in 'true'])
    love_matches = len([ x for x in user_name.lower() + crush_name.lower() if x in 'love'])

    total = int( str(true_matches) + str(love_matches) )

    extra_str = '.'
    if total < 10 or total > 90 :
        extra_str = ', you go together like coke and mentos.'
    elif total >= 40 or total <= 50 :
        extra_str = ', you are alright together.'

    print(f'Your Love Score is {total}{extra_str}')


loveCalculator()