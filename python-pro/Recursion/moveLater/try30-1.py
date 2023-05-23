num = 23
start = 2
box = start
g = 0
i = 1
while box < num:
    i += 1
    if box % i == 0:
        box += i
        g += 1
        i = 1

print(g)
