secret_word = 'olive'
nn=0
for cake in secret_word:
    tt=nn + secret_word.count(cake)
    print('letter: ' + cake)
    print(tt)

p=len(secret_word)
print(p)

print('hello world')

s = 'garage'
ll = 0
for char in s:
    kk = ll + s.count(char)
    print(kk)

letters ='ABC'
digits = '123'
for letter in letters:
    for digit in digits:
        print(letter + digit)

title = 'The Escape'
total = 0
for char1 in title:
    for char2 in title:
        print(char1 + char2)
        total = total + 1
    print(total)
