




val = [10, 40 ,30 ,50, 20]
freq = [1, 2 ,3 ,4 ,5]
def interQuartile(values, freqs):
    new=[]
    for b,a in enumerate(values):
        for z in range(freqs[b]):
            new.append(a)
    return new



data = interQuartile(val,freq)
n = len(data)
slist = sorted(data)


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
    slist.remove(check)
    q1 = []
    q2 = []
    for i in slist:
        if i >= check:
            q2.append(i)
        else:
            q1.append(i)
    n1 = len(q2)
    n2 = len(q1)
    return quartiles(n1, q2), quartiles(n2, q1)


bob = (quartiles(n, slist))
answer = list(findq(slist))
ra = sorted(answer)
a = [float(b) for b in ra]

print(round(max(a)-min(a),1))