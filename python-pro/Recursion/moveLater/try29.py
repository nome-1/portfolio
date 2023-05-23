chef = 100
store2 = 200
n = int(input())
for i in range(n):
    a, b = input().split()
    a = float(a) / 100
    b = float(b) / 100
    sale1 = chef * (a)
    discount1 = chef - sale1
    discount1 = round(discount1)
    sale2 = store2 * (b)
    discount2 = store2 - sale2
    discount2 = round(discount2)
    if discount1 < discount2:
        print("FIRST")
    elif discount1 == discount2:
        print("BOTH")
    else:
        print("SECOND")
