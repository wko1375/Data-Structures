def sumsquares(n):
    if n==1:
        return 1
    else:
        return n**2 + sumsquares(n-1)

def sumsquareslst(n):
    return sum([x**2 for x in range (n+1)])

def sumsquaresodd(n):
    finalval = 0
    for i in range(1, n+1, 2):
        finalval += i**2
    return finalval

def sumsquaresoddlst(n):
    return sum([x**2 for x in range (1, n+1, 2)])



print(sumsquaresodd(10))
