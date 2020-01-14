def encrypt(s):
    reverse_str_list = list(s[::-1])
    d = {'a': '0', 'e': '1', 'o': '2', 'u': '3'}
    i = 0

    for char in reverse_str_list:
        if char.lower() in d.keys():
            reverse_str_list[i] = d[char]
        i += 1

    return ''.join(reverse_str_list) + 'aca'
