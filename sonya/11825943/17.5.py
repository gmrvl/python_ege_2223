file = open('17.5.txt')

last = -1
counts = 0
maxsumm = 0
s = 0
i = 0
for nb in file:
    nb = int(nb)
    if nb % 2 == 0:
        s += nb
        i += 1
srarifm = s / i
for n in file:
    n = int(n)
    if last > -1:
        if last % 3 == 0 or n % 3 == 0:
            if last < srarifm or n < srarifm:
                counts += 1
                summ = last + n
                if summ > maxsumm:
                    maxsumm = summ
    last = n
print(counts, maxsumm)
