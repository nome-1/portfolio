i = 1
tail = 0
while i < 20:
    if tail is not None:
        break
    tail = i
    i += 1
print(tail)