i = [6, 12, 8 ,10, 20 ,16]
freak = [5 ,6 ,7 ,8, 9 ,10]
def bob(i,freak):
    new = []
    for b, a in enumerate(i):
        for z in range(freak[b]):
            new.append(a)
    return new


data = bob(i,freak)

n = len(data)

slist = sorted(data)
print(slist)

def quartiles(n, arr):
    if n % 2 == 1:
        dmid = round(n / 2)
        middle = round(dmid)
        return (arr[middle])
    else:
        mid = int(n / 2) - 1
        m1 = (arr[mid] + arr[mid + 1])
        m2 = m1 / 2
        return (m2)


def findq(slist):
    check = quartiles(n, slist)
    ff=[]
    for k in slist:
        if k !=check:
            ff.append(k)
    q1 = []
    q2 = []
    for i in ff:
        if i >= check:
            q2.append(i)
        else:
            q1.append(i)
    n1 = len(q2)
    n2 = len(q1)
    return quartiles(n1, q2), quartiles(n2, q1)


bob = (quartiles(n, slist))
print(bob)
answer = list(findq(slist))
print(answer)
ra = sorted(answer)
print(ra)
a = [int(b) for b in ra]
print(a)
vv=(max(a)-min(a))
print(vv)