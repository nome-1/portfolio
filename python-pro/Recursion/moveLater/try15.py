bob=[1,0,6,0,6,6,0,4]
print(len(bob))
i=0
while i<len(bob):
    if bob[i] == 0:
        bob.insert(i,0)
        bob.pop()
        i+=2
    else:
        i+=1

print(bob)
print(len(bob))