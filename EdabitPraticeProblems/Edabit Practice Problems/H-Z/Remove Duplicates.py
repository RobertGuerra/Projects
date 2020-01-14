from collections import OrderedDict


def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))

#Difference between this and set is this process maintains order

