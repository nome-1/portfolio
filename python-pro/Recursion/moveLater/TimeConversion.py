def timeConversion(s):
    con=""
    if s[8:]=="AM":
        if s[0:2]=="12":
            con=s.replace(s[0:2], "00")
        else:
            con=s
    elif s[8:]=="PM":
        if s[0]=="0":
            b=1200
            for i in range(int(s[1])):
                b+=100
            b=str(b)
            con = s.replace(s[0:2],str(b[0:2]))
        elif s[0]=="1":
            b = 1200
            if int(s[0:2])==12:
                con=s
            else:
                for i in range(int(s[0:2])):
                    b += 100
                b = str(b)
                con = s.replace(s[0:2], str(b[0:2]))
    return con[0:8]


s = "12:00:45AM"
print(timeConversion(s))
