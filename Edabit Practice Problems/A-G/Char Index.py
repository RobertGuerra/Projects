def char_index(word, char):
    a = 0
    b = 0
    i = 0
    while word[i] != char:
        if i == len(word) - 1:
            return None
        i += 1
    a = i

    word = word[::-1]

    j = 0
    while word[j] != char:
        j += 1
    b = len(word) - (j + 1)

    return [a, b]