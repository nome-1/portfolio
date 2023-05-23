# dead box a=[1,2,3,4,3,2,1] o(n) sol put new value in a box.
# if value already in the box remove it and update ban list
# or count(n) if val less then 1 = answer
import numpy as np
a = [1, 2, 3, 4, 3, 2, 1,4,5]
an=np.unique(a)
box=[]
check=[]
for i in a:
    if i in box:
        check.append(i)
    else:
        box.append(i)
tm=[w for w in a if w not in check]
print(tm[0])