from collections import Counter

l = ['Boston Americans', 'New York Giants', 'Chicago White Sox', 'Chicago Cubs', 'Chicago Cubs', 'Pittsburgh Pirates',
     'Philadelphia Athletics', 'Philadelphia Athletics', 'Boston Red Sox', 'Philadelphia Athletics', 'Boston Braves',
     'Boston Red Sox', 'Boston Red Sox', 'Chicago White Sox', 'Boston Red Sox', 'Cincinnati Reds', 'Cleveland Indians',
     'New York Giants', 'New York Giants', 'New York Yankees', 'Washington Senators', 'Pittsburgh Pirates',
     'St. Louis Cardinals', 'New York Yankees', 'New York Yankees', 'Philadelphia Athletics', 'Philadelphia Athletics',
     'St. Louis Cardinals', 'New York Yankees', 'New York Giants', 'St. Louis Cardinals', 'Detroit Tigers',
     'New York Yankees', 'New York Yankees', 'New York Yankees', 'New York Yankees', 'Cincinnati Reds',
     'New York Yankees', 'St. Louis Cardinals', 'New York Yankees', 'St. Louis Cardinals', 'Detroit Tigers',
     'St. Louis Cardinals', 'New York Yankees', 'Cleveland Indians', 'New York Yankees', 'New York Yankees']

c = Counter(l)
print(c)

arrayV = [1, 3, 5]
arrayW = [2, 4, 6]
z = list(zip(arrayV, arrayW))
zone = 0
arrayVW = []
arrayVWT = 0
arrayWT = 0
for i in z:
    arrayVW.append((z[zone][0]) * (z[zone][1]))
    zone += 1

for t in arrayVW:
    arrayVWT += t

for l in arrayW:
    arrayWT += l

zf=round(arrayVWT / arrayWT,1)
print(zf)
