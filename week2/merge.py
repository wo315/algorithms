# merge.py -- Ex2.3-2
def merge_modify(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(A):
    if len(A) <= 1:
        return A
    mid = int(len(A)/2)
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])
    return merge_modify(left, right)
