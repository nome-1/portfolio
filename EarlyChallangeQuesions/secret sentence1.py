s = 'zephyr'
for i in range(0, len(s), 3):
    print(s[i])

for N in range(len(s) - 1, -1, -1):
    print(s[N])

s = 'zephyr'
i = 0
while i < len(s):
    print('We have ' + s[i])
    i = i + 3

i=len(s)-1
while i>=0:
    print('We have '+ s[i])
    i=i-1

i = 0
while i < len(s) and s[i] != 'y':
    i = i + 1
    print(i)

sentence = input()
result = ''
i = 0
while i < len(sentence):
    result = result + sentence[i]
    if sentence[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1
print(result)

songs = 'ABCDE'
while True:
    button = int(input())
    if button == 4:
        break
    presses = int(input())
    for i in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]
output = ''
for song in songs:
    output = output + song + ' '
print(output[:-1])

i=0
while i<3:
    j=10
    while j<=50:
        print(j)
        if j==30:
            break
        j=j+10
    i=i+1
