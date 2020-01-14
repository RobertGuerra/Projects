def make_change(c):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while c >= 25:
        c = c - 25
        quarters += 1
    while c >= 10:
        c = c - 10
        dimes += 1
    while c >= 5:
        c = c - 5
        nickels += 1
    while c >= 1:
        c = c - 1
        pennies += 1

    return {'q': quarters, 'd': dimes, 'n': nickels, 'p': pennies}


print(make_change(389))
