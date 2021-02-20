def compress(p, a, b, k, n):
    num = ( (a*k + b) % p) % n
    return num
def f(x):
    if x == 1:
        return 3
    else:
        return 2 * f(x-1) + 6*x
def main():
    print(f(5))

main()
