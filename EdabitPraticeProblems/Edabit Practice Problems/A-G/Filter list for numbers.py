def filter_list(lst):
    return [item for item in lst if type(item) == int]


print(filter_list([1, 2, 3, 'org', '1', 33, 'four']))

#return value: [1, 2, 3, 33]
