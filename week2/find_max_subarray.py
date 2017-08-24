#divide and conquer method to solve the problem
def find_max_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low + high)/2)
        left_low, left_high, left_sum    = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -100000
    left_total = 0
    max_left = 0
    for i in range(mid, 0, -1):
        left_total += A[i]
        if left_total > left_sum:
            left_sum = left_total
            max_left = i
    right_sum = -10000
    right_total = 0
    max_right = 0
    for j in range(mid+1, len(A)):
        right_total += A[j]
        if right_total > right_sum:
            right_sum = right_total
            max_right = j
    return max_left, max_right, left_sum + right_sum

if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    a, b, c = find_max_subarray(A, 0, 15)
    print(a, b)
    print(c)
