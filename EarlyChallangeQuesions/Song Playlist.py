songs = 'ABCDE'
songs = songs[1] + songs[2] + songs[3] + songs[4] + songs[0]
print(songs)

s= 'abcdefghijk'
print(s[4:8])
print(s[:])
print(s[4:])
print(s[-50:3])

ba='abcde'
ba=ba[1:] + ba[0]
print(ba)

k=False
run=0
while not k:
    print('kate')
    run= run +1
    if run==5:
        break

valid = False
while not valid:
    m1 = input()
    valid = len(m1) == 5 and m1[:2] == 'xy'
