def index_multiplier(lst):
    summ = 0
    iterator = 0

    if lst is None:
        return 0
    else:
        for num in lst:
            summ += num * iterator
            iterator += 1

    return summ


#def index_multiplier(lst):
#  return sum([lst[c]*c for c in range(len(lst))])

#def index_multiplier(lst):
#  return sum(j*i for i, j in enumerate(lst))
