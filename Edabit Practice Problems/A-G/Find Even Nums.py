def find_even_nums(n):
    evens = [number * 2 for number in range(1, int(n / 2) + 1)]

    return evens


print(find_even_nums(0))
