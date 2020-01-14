def is_strange_pair(txt1, txt2):
    try:
        return txt1[0] == txt2[len(txt2) - 1] and txt2[0] == txt1[len(txt1) - 1]
    except IndexError:
        return txt1 == txt2

#Example of a strange pair: "ratio orator"
