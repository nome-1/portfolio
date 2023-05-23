n = False or True
print(n)

d = 7
if d == 8 or d == 9:
    print('true')
else:
    print('false')

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
# Telemarketer number: first digit 8 or 9, fourth digit 8 or 9,
# second digit and third digit are same

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print('ignore')
else:
    print('answer')
