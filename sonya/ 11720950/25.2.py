 # Переписала
for i in range(210235, 210301):
    k = 0
    sq = int(i ** 0.5)
    a = []
    for n in range(2, sq):
        if i % n == 0:
            k += 1
            a.append(i // n)
            a.append(i // (i // n))
    if k == 2:
        print(a)


