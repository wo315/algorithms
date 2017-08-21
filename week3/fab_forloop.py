# fab_forloop
def fabonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    while n >= 3:
        a, b = a + b, a
        n -= 1
    return a
