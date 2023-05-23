Y=int(input())
L=(0<=Y<=50)
print(L)
M=int(input())
LL=(Y<=M<50)
print(LL)

def ages(a,b):
    d = b - a
    if a == b:
        print(a)
    else:
        print(b + d)

age1 = int(input())
age2 = int(input())
ages(age1,age2)