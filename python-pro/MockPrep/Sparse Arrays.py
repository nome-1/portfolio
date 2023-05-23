import re

# The search() function returns a Match object:

txt = "The rain zThe in Spain"
x = re.findall("The", txt)
print(x)
print(len(x))
f = ['aba', 'baba', 'aba', 'xzxb']
t = " ".join(f)
print(t)
q = ['aba', 'xzxb', 'ab']
for i, b in enumerate(q):
    a = re.findall(b, t)
    print(len(a))

# ----------
string = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']



def matchingStrings(strings, queries):
    li = []
    for i, b in enumerate(queries):
        a = strings.count(b)
        li.append(a)
    return li


print(matchingStrings(string, queries))
