def flip_end_chars(txt):
    if len(txt) < 2:
        return 'Incompatible'
    elif txt[1] == txt[-1]:
        return 'Two\'s a pair.'
    else:
        return txt[-1] + txt[1: len(txt) - 2] + txt[0]
