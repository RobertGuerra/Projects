# simple program that with a function that takes one parameter
# and using a while loop cumilatively appends the sum of the next number
# and will print list and append the cumilative sum at the end
# of the list

def cumulative_sum(lst):
    new_lst = []
    i = 1
    while i <= len(lst):
        new_lst.append(sum(lst[0:i]))
        i += 1

    return new_lst


print([1, 2, 3, 0, -32, 11, 12])
print(cumulative_sum([1, 2, 3, 0, -32, 11, 12]))
