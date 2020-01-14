def say_hello_bye(name, num):
    #name = name[0].upper() + name[1:len(name)]
    name = name.title()
    if num is 1:
        return "Hello {}".format(name)

    return "Bye {}".format(name)


print(say_hello_bye('roger', 1))
