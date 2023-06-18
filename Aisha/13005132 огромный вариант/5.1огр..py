for i in range (1, 1000):
    n = bin(i)[2:]
    n = str(n)
    n += n[-1]
    summa = 0
    for z in range(len(n)):
        summa += int(n[z])
    n += str(summa % 2)
    r = int(n, 2)
    if r > 105:
        print(r)
        break