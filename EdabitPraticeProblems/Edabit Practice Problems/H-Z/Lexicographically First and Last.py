def first_and_last(s):
    first, last = [], []

    for char in s:
        first.append(char)
    first.sort()
    last = first[::-1]

    return [''.join(first), ''.join(last)]
