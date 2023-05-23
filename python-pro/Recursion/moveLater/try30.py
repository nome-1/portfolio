num=23
start=2
box=start
g=0
while box<num:
    for i in range((num)):
        if i>1:
            if box%i==0:
                box+=i
                g+=1
                break
print(box)
print(g)