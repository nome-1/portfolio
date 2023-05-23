box = [1,2,3,0,0,0]
boz = [2,5,6]
nums1 = []
tt=[king for king in box[0:3]]
for z in range(8):
    if z>=len(boz):
        break
    else:
        tt.insert(3,boz[z])
rm=sorted(tt)
print(rm)

for i in range(max(len(boz), len(box))):
    try:
        nums1.append(box[i])
    except:
        pass
    if i >= len(boz):
        break
    else:
        nums1.append(boz[i])
nums1.sort()
print(nums1)

t=[x for x in boz+box if x!=0]
t.sort()
print(t)