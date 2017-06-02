"""P22作业第二题，非升序"""
def insertion_sort(A):
    n = len(A)
    i = 0
    j = 1
    for j in range(n):
        
        i = j-1
        key = A[j]
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key 
    return A
