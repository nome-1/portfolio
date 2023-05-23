def average(array):
    narray=set(array)
    s=sum(narray)
    l=len(narray)
    value=(s/l)
    mm=round(value,3)
    return mm
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)