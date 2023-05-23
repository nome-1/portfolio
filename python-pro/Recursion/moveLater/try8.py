import math
val = [10, 40, 30, 50, 20]
n = len(val)


def mean(val, n):
    return sum(val) / n
km=(mean(val, n))
box=[]
for i in range(len(val)):
    box.append((val[i]-km)**2)
bb=(mean(box,len(box)))
print(round(math.sqrt(bb),1))