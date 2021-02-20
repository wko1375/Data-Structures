def split_parity(lst):
    n = 0
    while n < len(lst):
        if lst[n] % 2 == 0:
            count = n
            while count < len(lst):
                if lst[count] % 2 != 0:
                    a = lst[count]
                    lst[count] = lst[n]
                    lst[n] = a
                    break
                count += 1
        n += 1
    return lst
