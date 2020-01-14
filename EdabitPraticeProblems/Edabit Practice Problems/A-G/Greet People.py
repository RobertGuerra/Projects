def greet_people(names):
    greet_list = []
    for name in names:
        greet_list.append("Hello {}".format(name))

    return ', '.join(greet_list)


#-------Example Outputs--------

#greet_people(["Joe"]) ➞ "Hello Joe"

#greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"

#greet_people(["Frank", "Angela", "Joe"]) ➞ "Hello Frank, Hello Angela, Hello Joe"
