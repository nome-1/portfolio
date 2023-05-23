n = int(input().strip())

a = list(map(int, input().rstrip().split()))


def numswap(n, a):
    runs = 0
    change = 0
    box = 0
    for z in range(n):
        for i, b in enumerate(a):
            if i == len(a) - 1:
                if change > 0:
                    runs += 1
                    box += change
                    change = 0
                    break
                break
            if a[i + 1] < a[i]:
                a[i + 1], a[i] = a[i], a[i + 1]
                change += 1
    print(f"Array is sorted in {box} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


numswap(n, a)
# a=[4,3,1,2] n=4