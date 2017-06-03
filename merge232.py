"""
作业2.3-2，重写过程merge，使之不使用哨兵
"""

def merge232(s, p, q, r):
    n1 = q - p + 1
    n2 = r - q
#    n3 = r - p
    L = s[:n1]
    R = s[n2:]
    j = 0
    k = 0
    
    for i in range(r+1):
        if L[j] <= R[k]:
            s[i] = L[j]
            j += 1
            if j >= n2:
                s[i+1:] = R[k:]
                return s
        else:
            s[i] = R[k]
            k += 1
            if k >= n1:
                s[i+1:] = L[j:]
                return s

