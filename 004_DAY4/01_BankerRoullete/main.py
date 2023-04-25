import random

names = input("Give me everybody's names, separated by a comma.\n")
names_list = names.replace(', ', ',').split(',')

def getRandom():
    num = random.randint(0, len(names_list) - 1)
    return names_list[ num ]

print(f'\n{ getRandom() } is going to buy the meal today!')
print('')