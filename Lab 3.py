def zerosort(lst):
    end = False
    nextzero = False
    if lst[1] == 0:
        nextzero = True
    i = 0
    while end == False:
        if nextzero == False:
            if lst[i] == 0:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


print(zerosort([0,1,0,0,3,13]))
