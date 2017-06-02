"""insertion sort"""
def insertion_sort(A):
    n = len(A)
    j = 1
    i = 0
    for j in range(n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
