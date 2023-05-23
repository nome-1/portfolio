n=439
box=[]
nh=[]
while n>0:
    box.append(n%2)
    n=n//2
tom=(box[::-1])
pat=0
for b,i in enumerate(tom):
    if i !=0:
        pat+=1
        if b==len(tom)-1:
            nh.append(pat)
    else:
        nh.append(pat)
        pat=0
print(max(nh))