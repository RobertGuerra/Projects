from math import floor, log


def count_ones(num):
    ones = 0
    power = floor(log(num, 2))
    while num > 0:
        if 0 <= num % 2 ** power < num:
            num -= 2 ** power
            power -= 1
            ones += 1
        else:
            power -= 1

    return ones


print(count_ones(2017))
