def steps_to_convert(txt):
    lower = 0
    upper = 0

    for char in txt:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            pass

    if upper > lower:
        return lower
    else:
        return upper
