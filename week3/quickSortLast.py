#quickSortLast -- the pivot is the last element
def quick_last(A):
    if len(A) <= 1:
        return A, 0
    mid, total = partition(A)
    left, left_num = quick_last(A[:mid])
    right, right_num = quick_last(A[mid+1:])
    result = left + [A[mid]] + right
    summary = total + left_num + right_num
    return result, summary

def partition(A):
    pivot = A[-1]
    i = 0
    for j in range(len(A) - 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[-1] = A[-1], A[i]
    return i, j + 1

if __name__ == '__main__':
    lines = [line.rstrip() for line in open("QuickSort.txt")]
    A = [int(p) for p in lines]
    B = quick_last(A)
    print(B)
