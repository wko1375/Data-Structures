def flat_list(nested_lst, low, high):
    lst = []
    if low == high:
        if isinstance(nested_lst[low], list):
            x = flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
            lst.extend(x)
            return lst
        else:
            lst.append(nested_lst[low])
            return lst
    else:
        if isinstance(nested_lst[low], list):
            x = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
            lst.extend(x)
            y = flat_list(nested_lst, low+1, high)
            lst.extend(y)
            return lst
        else:
            lst.append(nested_lst[low])
            lst.extend(flat_list(nested_lst, low+1, high))
            return lst









print(flat_list( [ [1,2] ,3 , [4,[5,6,[7],8] ] ], 2, 2))
