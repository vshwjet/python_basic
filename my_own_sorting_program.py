

def sorting(list_to_be_sorted):
    sorted_list = []
    while len(list_to_be_sorted) != 0:
        s = 0
        for i in list_to_be_sorted:
            if i > s:
                s = i
        list_to_be_sorted.remove(s)
        sorted_list.append(s)
    sorted_list.reverse()
    return sorted_list


