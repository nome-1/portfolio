def selection(list):
    for i in range(len(list)):
        min_i = i
        for j in range(i + 1, len(list)):
            if list[min_i] > list[j]:
                min_i = j
        list[i], list[min_i] = list[min_i], list[i]
    print(list)


bob = [1, 5, 3, 6, 8, 2]
selection(bob)
