import math
def factors(num):
    n = 1
    while n < math.sqrt(num)+1:
        if num % n == 0:
            yield n
        n+=1
    n = int(math.sqrt(num))-1
    while n > 0:
        if num % n == 0:
            yield int(num/n)
        n-=1
