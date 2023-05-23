import io
import sys

with open('bob.txt', 'r') as sys.stdin:
    a = list(map(int, input().split()))
    m = a[1]
    b = []
    n = []
    for i in range(a[0]):
        b.append(list(map(int, input().split())))

    for i in range(len(b)):
        for a in range(1):
            n.append(max(b[i]) ** 2)
    print(n)
    g = sum(n)
    print(g)
    print(g % m)
