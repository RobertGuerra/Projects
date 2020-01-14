def XO(txt):
    num_of_x = 0
    num_of_o = 0
    for char in txt:
        if char == 'X' or char == 'x':
            num_of_x += 1
        elif char == 'O' or char == 'o':
            num_of_o += 1
        else:
            pass

    return num_of_x == num_of_o


print(XO('xo'))
