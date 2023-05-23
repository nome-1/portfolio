import math
import os
import random
import re
import sys

data = [3, 7, 8, 5, 12, 14, 21, 13, 18]
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
    if len(slist) % 2 == 1:
        slist.remove(check)
    q1 = []
    q2 = []
    for i in slist:
        if i >= check:
            q2.append(i)
        else:
            q1.append(i)
    n1 = len(q1)
    n2 = len(q2)
    return quartiles(n1, q1), quartiles(n2, q2)


bob = (quartiles(n, slist))
answer = list(findq(slist))
answer.append(bob)
ra = sorted(answer)
a = [int(b) for b in ra]
for i in a:
    print(i)
