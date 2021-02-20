def findChange(lst01):
    n = 1
    count = 0
    while n < len(lst01):
        if lst01[n-1] == 1:
            return n-1
        if lst01[n] == 1:
            return n
        if lst01[n+1] == 1:
            return n+1
        n += 3
