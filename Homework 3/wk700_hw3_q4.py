def c(a, b):
    if a<b:
        return a
    if b<a:
        return b
    else:
        return a

def list_min(lst,low,high):
    m = c(lst[low],lst[high])
    if high-low == 1:
        m = c(m,lst[low])
        m = c(m,lst[high])
        return m
    else:
        if lst[low]<lst[high]:
            m = lst[low]
            m = list_min(lst,low,high-1)
        if lst[high]<lst[low]:
            m = lst[high]
            m = list_min(lst,low+1,high)
        return m
