import numpy


def arrays(arr):
    b = numpy.array(arr, float)
    a = numpy.flip(b, 0)
    return a

    # complete this function
    # use numpy.array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)