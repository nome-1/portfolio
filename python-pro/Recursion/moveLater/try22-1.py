fog = "132 456 Wq  m e"
t = fog.split(" ")
print(t)
tom=""
for i in t:
    if i.isalpha():
        for z in range(1):
            tom+=(i[z].upper()+i[z+1:]+" ")
    else:
        tom+=i+" "
print(tom)
print(len(tom))