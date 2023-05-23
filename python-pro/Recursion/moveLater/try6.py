import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)
print(sum(twoDArray[2]))

def traverseTDArray(accounts):
    custl=[]
    l=0
    for i in range(len(accounts)):
        if i >0:
            custl.append(l)
            l=0
        for j in range(len(accounts[0])):
            l+=(accounts[i][j])
    if l>0:
        custl.append(l)
    print(max(custl))



traverseTDArray(twoDArray)