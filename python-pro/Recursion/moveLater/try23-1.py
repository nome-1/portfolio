
dog = "1 0 2 $ 3 1 "
lm = dog.replace(" ", "")
print(dog)
print(lm)

for t in range(len(lm)):
    try:
        print(int(int(lm[t + t]) / int(lm[t + t + 1])))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except TypeError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
    except IndexError:
        break
