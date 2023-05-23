import numpy as np

num1 = int(input())
x1 = 'far'
x2 = ','
x3 = str

m1 = (x1 * num1)
m2 = (x2 * (num1 - 1))
a1 = [m1]
a2 = [m2]


def counttist(a1, a2):
    return np.array([[i, j] for i, j in zip(a1, a2)]).ravel()


mk1 = (counttist(a1, a2))
print(mk1)


def listToString(mk1):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in mk1:
        str1 += ele

    # return string
    return str1


print(listToString(mk1))
