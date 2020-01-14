def sort_by_length(lst):
    length_list = sorted([len(item) for item in lst])
    sorted_list = []
    for length in length_list:
        for item in lst:
            if len(item) == length:
                sorted_list.append(item)
            else:
                pass

    return sorted_list


print(sort_by_length(['Ca', 'Cowabunga', 'Nuts', 'Tir']))


