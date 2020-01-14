def sum_two_smallest_nums(lst):
    new_list = [number for number in lst if number > 0]

    new_list.sort()

    return new_list[0] + new_list[1]