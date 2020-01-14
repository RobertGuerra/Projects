def remove_special_characters(txt):
    txt1 = ''
    for char in txt:
        if char.isalnum() or char.isspace():
            txt1 += char
        elif char in ('_', '-'):
            txt1 += char
        else:
            pass

    return txt1


print(remove_special_characters('The quick brown fox!'))
