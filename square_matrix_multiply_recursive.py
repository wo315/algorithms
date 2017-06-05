def square_matrix_multiply_recursive(A, B):
	n = len(A)
	C = [None] * n

	A11 = []
	A12 = []
	A21 = []
	A22 = []
	B11 = []
	B12 = []
	B21 = []
	B22 = []
	'''
	C11 = []
	C12 = []
	C21 = []
	C22 = []
	'''
	for item in range(len(C)):
		C[item] = [0] * n
	print(C)
	if n == 1:
		C[0][0] = A[0][0] * B[0][0]
	else:
		for i in range(n//2):
			A11.append(A[i][0:n//2])
			A12.append(A[i][n//2:])
			B11.append(B[i][0:n//2])
			B12.append(B[i][n//2:])

			C11.append(C[i][0:n//2])
			C12.append(C[i][n//2:])
		for j in range(n//2, n):
			A21.append(A[j][0:n//2])
			A22.append(A[j][n//2:])
			B21.append(B[j][0:n//2])
			B22.append(B[j][n//2:])

			C21.append(C[j][0:n//2])
			C22.append(C[j][n//2:])
		C11 = square_matrix_multiply_recursive(A11, B11) + square_matrix_multiply_recursive(A12, B21)
		C12 = square_matrix_multiply_recursive(A11, B12) + square_matrix_multiply_recursive(A12, B22)
		C21 = square_matrix_multiply_recursive(A21, B11) + square_matrix_multiply_recursive(A22, B21)
		C22 = square_matrix_multiply_recursive(A21, B12) + square_matrix_multiply_recursive(A22, B22)

	return C
		#print(A11,A12,A21,A22,B11,B12,B21,B22)
A = [[1,2,3,4], [2,3,4,1],[3,4,1,2],[4,1,2,3]]
b = square_matrix_multiply_recursive(A,A)