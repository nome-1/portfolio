# first test run of list comp
fog = "hello world lol"
t = fog.split(" ")
print(t)
print(len(t))
s=([x[0].upper()+x[1:] if x[0].isalpha() else x for b,x in enumerate(t)])
tom=""
for d in s:
    tom+=(d+" ")
print(tom)
