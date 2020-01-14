def is_narcissistic(n):
    s = str(n)
    l = len(s)
    sum_of_numbers = 0
    m = 0

    debug_list = []
    for char in s:
        m = int(char) ** l
        sum_of_numbers += m
    print("{} = {}".format(sum_of_numbers, n))
    return n == sum


print(is_narcissistic(66))
