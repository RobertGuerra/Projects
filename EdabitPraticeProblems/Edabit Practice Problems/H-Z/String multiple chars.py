def double_char(txt):
    char_list = []
    for char in txt:
        char_list.append(char)
        char_list.append(char)

    return ''.join(char_list)