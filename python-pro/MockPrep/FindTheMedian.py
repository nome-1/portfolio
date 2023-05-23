
def findMedian(arr):
    t=sorted(arr)
    print(t)
    f=int(len(t)/2)
    print(f)
    print(t[f])



a=[0,1,2,4,6,5,3,8,12]
print(findMedian(a))