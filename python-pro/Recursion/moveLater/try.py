from collections import Counter

n = 10
x = "64630 11735 14216 99233 14470 4978 14216 38120 51135 64630"
rm = x.split()  # makes a list
gg = [int(b) for b in rm]  # turns string list to int lsit
s1list = (sorted(gg))  # sort list
slist = [int(a) for a in s1list]  # turns list from float to int


def mean(n, gg):
    total = 0
    for i in gg:
        total += i
    print(float(total / n))


def median(n, slist):
    dmid = int(n / 2) - 1  # remember 0
    if n % 2 == 1:
        middle = round(dmid)
        print(slist[middle])
    else:
        m1 = (slist[dmid] + slist[dmid + 1])
        m2 = m1 / 2
        print(m2)


def mode(slist):
    c = Counter(slist)
    box = []
    b = 0
    for letter in slist:
        if c[letter] > 1:
            box.append(letter)
            b += 1
    if b >= 1:
        print(min(box))
    else:
        print(min(slist))


mean(n, gg)
median(n, slist)
mode(slist)
