def first_arg(*args):
    try:
        return args[0]
    except IndexError:
        return None


def last_arg(*argc):
    try:
        return argc[len(argc) - 1]
    except IndexError:
        return None
