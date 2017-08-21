def partition(A):
    if len(A) <= 1:
        return
    A[0], A[-1] = A[-1], A[0]
    i = 1
    for j in range(1,len(A)):
        if A[j] < A[0]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[0], A[i-1] = A[i-1], A[0]
    return i - 1, j

def quickSort(A):
    if len(A) <= 1:
        return A, 0
    mid, comp = partition(A)
    left, left_num = quickSort(A[:mid])
    right, right_num = quickSort(A[mid+1:])
    pivot = [A[mid]]
    B = left + pivot + right
    count = left_num + right_num + comp
    return B, count


