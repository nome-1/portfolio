
def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f"item found at Index {i}"
    return -1



print(linearSearch([20,40,30,50,90], 90))