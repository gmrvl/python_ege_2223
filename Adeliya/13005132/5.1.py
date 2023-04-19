for i in range(1, 100):
    n = str (bin(i)[2:])
    n += n[-1]
    summa = 0
    for j in range(len(n)):
        summa += int(n[j])
    n += str(summa % 2)
    r = int(n, 2)
    if r > 105:
        print(r)
        break