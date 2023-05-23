from notebook import Note
n1=Note("hello bird")
n2=Note("hello cat")
print(n1.id)
print(n1)
print(n2.id)
rm=n1.match("bird")
print(rm)
