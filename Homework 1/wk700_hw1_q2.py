
def shift(lst, k):
    for i in range(k):
        lst.append(lst[i])
    for i in range(k):
        lst.pop(0)
    return lst

def moreshift(lst, k, dir='left'):
    if dir == 'left':
        for i in range(k):
            lst.append(lst[i])
        for i in range(k):
            lst.pop(0)
        return lst
    else:
        for i in range(k):
            item = lst[len(lst)-1]
            lst.insert(0, item)
            lst.pop(len(lst)-1)
        return lst
