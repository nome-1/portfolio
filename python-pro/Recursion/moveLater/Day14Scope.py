arr = [1, 4, 7, 3, 5]
checkMax=0
for b, i in enumerate(arr):
    for a in arr[b+1:]:
        if abs(i - a)>checkMax:
            checkMax=abs(i-a)
print(checkMax)