n = int(input())
phone_book = {}
for i in range(n):
    name, number = input().split()
    phone_book[name] = number
Query = ""
for a in range(n):
    Query += input() + " "
tm = Query.split()
for g, m in enumerate(tm):
    try:
        print(f"{m}={phone_book[m]}")
    except KeyError:
        print("Not found")
#