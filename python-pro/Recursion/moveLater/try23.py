dog = "1 0 2 $ 3 1 "
lm = dog.replace(" ", "")
print(dog)
print(lm)
box = []
for i in (lm):
    try:
        box.append(int(i))
    except:
        box.append((i))
        pass
print(box)
j = 0
for t in range(len(box)):
    if t > 0:
        j = 1
    try:
        print(box[t + t] / box[t + t + 1])
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except TypeError as e:
        print("Error Code:", e)
    except IndexError:
        break
