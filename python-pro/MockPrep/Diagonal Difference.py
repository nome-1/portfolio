import numpy as np


def diagonaldifference(arr):
    dil=arr[0][0]
    dil2=arr[0][-1]
    # a = np.array(arr).reshape((3, 3))
    for i,b in enumerate(arr):
        print(dil,dil2)
        dil=dil[+1]
    print(arr[0][0], arr[1][1], arr[2][2])
    D1 =(arr[0][0] + arr[1][1] + arr[2][2])
    print(arr[0][2], arr[1][1], arr[2][0])
    D2 =(arr[0][2] + arr[1][1] + arr[2][0])
    print(D1,D2)
    return abs(D1 - D2)


print(diagonaldifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
