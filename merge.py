"""chapter2 basic P17"""
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q 
    L = A[:n1]
    R = A[n2:]
    L.append(float('inf'))
    R.append(float('inf'))
    k = p
    i = 0
    j = 0
    for k in range(r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    #return A

def merge_sort(A, p, r):
    if p < r:
        q = (r+p) // 2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
