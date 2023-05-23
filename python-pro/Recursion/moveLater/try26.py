box = ['apple', 'schtschurowskia', 'pllkisjh', 'tryst', 'cry']
comp=[]
vol = ["a", "e", "i", "o", "u"]
for a, x in enumerate(box):
    h = " ".join(box[a])
    tt = h.split()
    con = 0
    dim = []
    for w in tt:
        if w in vol:
            dim.append(con)
            con = 0
        else:
            con += 1
    try:
        comp.append(max(dim))
    except ValueError:
        comp.append(con)
for f in comp:
    if f<4:
        print("YES")
    else:
        print("NO")