def square_matrix_multiply(A, B):
    n = len(A)
    c = [None] * n
    for item in range(len(c)):
        c[item] = [0] * n
    #print(c)
    i, j, k = 0, 0, 0
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(n):
                c[i][j] += A[i][k] * B[k][j]
    return c
