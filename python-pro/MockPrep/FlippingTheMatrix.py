import numpy as np


def flipH(arr):
    box = []
    for i in range(1, len(arr) + 1):
        box.append(arr[-i])
    return box


def flipcolums(arr, index):
    b = 1
    for i in range(1, len(arr) + 1):
        if matrix[i - b][index] == matrix[-i][index] or matrix[i - b + 1][index] == arr[-i - 1]:
            break
        else:
            matrix[i - b][index], matrix[-i][index] = matrix[-i][index], matrix[i - b][index]


def flippingMatrix(matrix):
    a = np.array(matrix).reshape((4, 4))
    print(a)
    for i in range(len(matrix)):
        c = matrix[0][i], matrix[1][i]
        b = matrix[-1][i], matrix[-2][i]
        while i<1:
            for y in range(len(matrix)):
                if matrix[0][y] < matrix[-1][y] and matrix[1][y] < matrix[-2][y]:
                    arr = [x[y] for x in matrix]
                    flipcolums(arr, y)
            break
        if matrix[i][0] + matrix[i][1] < matrix[i][-1] + matrix[i][-2]:
            matrix[i] = flipH(matrix[i])
    b = np.array(matrix).reshape(4, 4)
    print(f"______________")
    total=b[0][0]+b[0][1]+b[1][0]+b[1][1]
    print(b)
    return total


#     # Write your code here


matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(flippingMatrix(matrix))
