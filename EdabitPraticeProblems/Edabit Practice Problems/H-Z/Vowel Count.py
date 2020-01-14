def count_vowels(txt):
    count = 0
    for char in txt:
        if char.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1

    return count
