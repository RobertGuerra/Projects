def duplicate_count(txt):
    duplicates = 0
    txt1 = set(txt)
    for char in txt1:
        if txt.count(char) > 1:
            duplicates += 1

    return duplicates


print(duplicate_count('Gulag Mansion says yeet'))
