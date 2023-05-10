for i in range(185311, 185331):
    a = [] # массив делителей
    stop = int(i ** 0.5)
    if stop == i**0.5:
        continue
    for d in range(1, stop + 1):
        if i % d == 0:
            a.append(d)
            a.append(i // d)
        if len(a) > 4:
            break

    if len(a) == 4:
        print(sorted(a))
