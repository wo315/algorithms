# recursion method
def fabonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)
