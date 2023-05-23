
def flipcolums(arr,index):
    print(arr)
    b=1
    for i in range(1,len(arr)+1):
        if matrix[i-b][index]==matrix[-i][index] or matrix[i-b+1][index]==arr[-i+1]:
            print(arr[-i+1])
            break
        else:
            print(matrix[i-b][index],matrix[-i][index])
            matrix[i-b][index]=matrix[-i][index]
    print(matrix)

matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
arr = [x[2] for x in matrix]
print(flipcolums(arr,2))