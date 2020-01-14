def format_num(n):
    n = list(str(n))
    n.reverse()
    num = []
    i = 2

    for item in n:
        num.append(item)

        if i % 3 == 1:
            num.append(',')

        i += 1

    num.reverse()
    return ''.join(num)


print(format_num(1000))
