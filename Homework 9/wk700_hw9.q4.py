def intersection_list(lst1, lst2):
    maximum_len = max(max(lst1), max(lst2))
    length = maximum_len + 1
    lst = [None] * length
    for index in range(len(lst1)):
        lst[lst1[index]] = lst1[index]
    intersection_list = []
    for index in range(len(lst2)):
        if lst[lst2[index]] != None:
            intersection_list.append(lst2[index])
    return intersection_list
