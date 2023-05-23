arr = [1, 2, 3, 4, 5]
x=0
a=[]
while x<len(arr):
    gg=arr.pop(0)
    a.append(sum(arr))
    arr.append(gg)
    x+=1
print(max(a),min(a))

print([tm for tm in arr])
