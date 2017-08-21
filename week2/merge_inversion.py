# Excerise 2.4
def merge_inversion(A):
    if len(A) <= 1:
        return A, 0
    mid = int(len(A)/2)
    left, left_num = merge_inversion(A[:mid])
    right, right_num = merge_inversion(A[mid:])
    merged, count = merge_sort(left, right)
    count += (left_num + right_num)
    return merged, count

def merge_sort(left, right):
    result = []
    total = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            total += (len(left) - i)
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result, total


if __name__ == '__main__':
    A = [4, 5, 7, 9, 7, 5, 1, 0, 7]
    print(merge_inversion(A))
