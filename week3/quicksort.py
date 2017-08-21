def quickSort(A):
    if A:
        pivot = A[0]
        lesser = [x for x in A[1:] if x <  pivot]
        greater = [x for x in A[1:] if x >= pivot]
        return quickSort(lesser) + [pivot] + quickSort(greater)
    else:
        return A
