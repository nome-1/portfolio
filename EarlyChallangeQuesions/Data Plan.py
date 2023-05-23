monthly_mb = int(input())
n = int(input())
excess = 0
for i in range(n):
    used = int(input())
    excess = excess + monthly_mb - used
print(excess + monthly_mb)


monthly_mb = int(input())
n1 = int(input())
total_mb = monthly_mb * (n1 + 1)
for i in range(n1):
    used = int(input())
    total_mb = total_mb - used
print(total_mb)
