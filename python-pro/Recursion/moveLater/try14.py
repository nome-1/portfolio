n=int(input())
s1=""
box=[]
for i in range(n):
    box.append(input().strip())
def convert(box):
    update=(list(box))
    return update

def finish(box):
    for a in range(len(box)):
        up=convert(box[a])
        i = 0
        firsth = ""
        secondh = ""
        while i<len(up):
            if i%2==0:
                firsth+=(up[i])
                i+=1
            else:
                secondh+=(up[i])
                i += 1
        print(firsth,secondh)

finish(box)