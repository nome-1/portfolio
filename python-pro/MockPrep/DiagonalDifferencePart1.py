

def diagonaldifference(arr):
    a=0
    b=0
    d1=[]
    d2=[]
    for i,j in enumerate(arr):
        dil = arr[a][b]
        dil2 = arr[a][-1 - b]
        d1.append(dil)
        d2.append(dil2)
        a+=1
        b+=1
    D1=sum(d1)
    D2=sum(d2)
    return abs(D1 - D2)

print(diagonaldifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


# def diagonalDifference(arr):
#     # Write your code here, O(n)
#     #l, r = left sum, right sum
#     l, r = 0, 0
#     # single pass, grab both values
#     for i in range(len(arr)):
#         l += arr[i][i]
#         r += arr[i][-i-1]
#     return abs(l-r)
#
#
#
#
#