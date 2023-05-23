import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

def traverseTDArray(accounts):
    box = []
    for i in range(len(accounts)):
        box.append(sum(twoDArray[i]))
    return max(box)


print(traverseTDArray(twoDArray))
