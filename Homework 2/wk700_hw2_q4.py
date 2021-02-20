def e_approx(n):
    sum = 1
    count = 1
    factsum = 1
    while count < n-1:
        factsum = count*factsum
        sum += 1/factsum
        count += 1
    return sum
