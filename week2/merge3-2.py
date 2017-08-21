# merge68.py -- another kind of mergesort

def mergesort(seq):
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)
    res = []
    while left and right:
        if left[-1] > right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res

if __name__ == '__main__':
    seq = [5, 2, 4, 7, 3, 1, 6, 2]
    print(mergesort(seq))
