def letter_check(lst):
    str1, str2 = lst[0].lower(), lst[1].lower()
    for char in str2:
        if char not in str1:
            return False

    return True
