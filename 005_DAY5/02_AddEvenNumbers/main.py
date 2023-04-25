
def sumEvens():
    total = 0

    for n in range(0, 101, 2):
        total += n

    return total

print( sumEvens() )