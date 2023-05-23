word = 'boat'
where = 2
lmk=word[where+1]
print(lmk)
tom=word[len(word)-2]
print(tom)

for num in range(1, 6):
    print(num)

for bf in range(0, 10, 2):
    print(bf)
for bff in range(10, 0, -1):
    print(bff)

n = int(input())
yesterday = input()
today = input()
occupied = 0
for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1
print(occupied)
