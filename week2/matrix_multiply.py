#for loop method calculate matrix-multiply
def matrix_multiply(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[0, 3, 1], [7, 0, 4], [9, 7, 0]]
    C = matrix_multiply(A, B)
    print(C)
