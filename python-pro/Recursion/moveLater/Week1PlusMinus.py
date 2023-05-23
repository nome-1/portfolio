arr = [-4, 3, -9, 0, 4, 1]
a = len(arr)


def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    a = len(arr)
    for b, i in enumerate(arr):
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1
    print(round(pos / a,6))
    print(round(neg / a,6))
    print(round(zero / a, 6))


plusMinus(arr)
