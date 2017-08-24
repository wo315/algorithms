# brute force method
def max_subarray(A):
    B = []
    for i in range(len(A)):
        if i == 0:
            continue
        B.append(A[i] - A[i-1])
    print(B)
    C = []
    for j in range(len(B)):
        a = B[j]
        for k in range(j+1, len(B)):
            a += B[k]
            C.append(a)
    print(C)
    print(len(C))
    print(max(C))
'''    maximum = C[0]
    for m in range(len(C)):
        if maximum <= C[m]:
            maximum = C[m]
''' 
    
if __name__ == '__main__':
    A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    max_subarray(A)

