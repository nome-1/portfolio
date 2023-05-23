n = int(input())
middle = (round((n / 2) + 0.1))
height = n
width = (n * 3)
mwidth = round((width / 2))
simble = ".|."
print(height, width, middle, mwidth)
for i in range(height):
    print('')
    for ia in range(width):
        if ia == mwidth and i + 1 == middle:
            print('WELCOME', ' ', end='')
        elif ia == mwidth and i + 1 != middle:
            print("|", ' ', end='')
        else:
            print('_', ' ', end='')

M, N = map(int, input().split())

for num in range(M):
    if num == (M - 1)/2:
        print("WELCOME".center(N, '-'))
    elif num < (M - 1)/2:
        print((".|."*((2*num) + 1)).center(N,'-'))
    else:
        print((".|." * (((2 * M) -1) - (2 * num))).center(N, '-'))