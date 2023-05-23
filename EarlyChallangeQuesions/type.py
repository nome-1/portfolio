lm=type(14)
print(lm)

yy=type(True)
print(yy)

tt= 5>2
print(tt)

mm= 6<3
print(mm)

m1= 5>=5
print(m1)

m2 = "hello" == "kelp"
print(m2)

at=20
bt=3
if at > bt:
    print('yes')

lt=20
mt=3
if mt < lt:
    print('es')
elif mt > lt:
    print('no')
else:
    print('clear')

apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one

if apple_total > banana_total:
    print('A')
elif banana_total > apple_total:
    print('B')
else:
    print('T')
