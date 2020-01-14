def mask(txt):
    if len(txt) <= 4:
        return txt

    txt = list(txt)
    txt.reverse()
    new_lst = []

    i = 0
    while i < 4:
        new_lst.append(txt[i])
        i += 1
    j = 0
    while j < len(txt) - 4:
        new_lst.append('#')
        j += 1

    new_lst.reverse()
    return ''.join(new_lst)
