def find_max_crossing_subarray(A, low, mid, high):
    left_sum, right_sum = -float('inf'), -float('inf')
    lsum, rsum = 0, 0
    i, j = mid, mid+1
    max_left, max_right = 0, 0
    while i >= low:
        lsum += A[i]
        if lsum > left_sum:
            left_sum = lsum
            max_left = i
        i -= 1 
    while j <= high:
        rsum += A[j]
        if rsum > right_sum:
            right_sum = rsum
            max_right = j
        j += 1
    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    mid = (low + high) // 2
    left_low, left_high, left_sum = 0,0,0
    cross_low, cross_high, cross_sum = 0,0,0
    right_low, right_high, right_sum = 0,0,0
    if high == low:
        return (low, high, A[low])
    else:
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and right_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
