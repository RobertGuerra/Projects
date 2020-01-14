def is_special_array(lst):
    length = len(lst)
    button = True

    i = 0
    while i < length:
        if lst[i] % 2 == 0 and button is True:
            button = not button
            i += 1
            continue
        elif lst[i] % 2 != 0 and button is False:
            button = not button
            i += 1
            continue
        else:
            return False

    return True


print(is_special_array([2, 7, 8, 7, 6, 1, 6, 3]))
