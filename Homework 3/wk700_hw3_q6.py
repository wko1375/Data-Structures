def appearances(s, low, high):
    d = dict()
    if high - low == 1:
        d[s[low]] = 1
        d[s[high]] = 1
        return d
    else:
        if s[low] in d:
            d[s[low]] += 1
        else:
            d[s[low]] = 1
        temp = appearances(s, low+1, high)
        for keya in d:
            if keya in temp:
                a = d[key] + temp[key]
                d.update(keya = a)









print(appearances("Hello world", 0, 10))
