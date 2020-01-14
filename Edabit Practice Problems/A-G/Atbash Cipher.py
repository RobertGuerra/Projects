
def atbash(txt):
    encryption_dict_upper = {}
    encryption_dict_lower = {}
    encrypted_message = []
    i = 0
    for num in range(65, 91):
        encryption_dict_upper.update({chr(num): chr(90 - i)})
        i += 1

    print(encryption_dict_upper)

    i = 0
    for num in range(97, 123):
        encryption_dict_lower.update({chr(num): chr(122 - i)})
        i += 1

    print(encryption_dict_lower)

    for char in txt:
        if char in encryption_dict_lower:
            encrypted_message.append(encryption_dict_lower[char])

        elif char in encryption_dict_upper:
            encrypted_message.append(encryption_dict_upper[char])
        else:
            encrypted_message.append(char)

    return ''.join(encrypted_message)


print(atbash('I would like some canes'))
