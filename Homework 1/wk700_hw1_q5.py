def fib(n):
    x, y = 1, 1
    val = 0
    while val < n:
        yield x
        x, y = y, x + y
        val += 1
