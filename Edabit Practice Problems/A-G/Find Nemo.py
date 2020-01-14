def find_nemo(sentence):
    i = 1
    sentence = sentence.split(" ")
    for word in sentence:
        if word == 'Nemo' or word == 'nemo':
            return "I found Nemo at {}!".format(i)
        i += 1

    return "I can't find Nemo :("


print(find_nemo('No nemo here!'))


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(9))

