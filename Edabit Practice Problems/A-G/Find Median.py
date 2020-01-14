from math import floor


def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[floor(len(lst) / 2)] + lst[floor(len(lst) / 2)] - 1) / 2

    return lst[floor((len(lst) - 1) / 2)]


print(median([20, 40, 20, 30, 50, 60, 70, 0, 20]))
