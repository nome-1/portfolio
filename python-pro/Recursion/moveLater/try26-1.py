comp = []
vol = ["a", "e", "i", "o", "u"]
for i in range(int(input())):
    n = int(input())
    tom = input()
    dim = []
    con = 0
    for w in tom:
        if w not in vol:
            dim.append(con)
            con += 1
        else:
            con =0
    try:
        comp.append(max(dim))
    except ValueError:
        comp.append(con)
for f in comp:
    if f < 4:
        print("YES")
    else:
        print("NO")



t = int(input())
vowels = {"a", "e", "i", "o", "u"}

for i in range(t):
    n = int(input())
    s = input()
    hard = 0
    for j in range(n):
        if (s[j] not in vowels):
            hard += 1
        else:
            hard = 0

        if (hard == 4):
            print("NO")
            break
    if (hard < 4):
        print("YES")
