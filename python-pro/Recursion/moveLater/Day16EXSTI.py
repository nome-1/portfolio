s=input()
try:
    int(s)
    print(s)
except ValueError:
    print("Bad String")