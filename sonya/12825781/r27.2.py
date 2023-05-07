file = open('272_A.txt')
N = int(file.readline())
ostatki = [0 for i in range(89)]
ostatkilen = [0 for z in range(89)]

summ = 0
lensumm = 0
for n in file:
    n = int(n)
    summ += n
    lensumm += 1
    if ostatki[summ % 89] == 0:
        ostatki[summ % 89] = summ
        ostatkilen[summ % 89] = lensumm

if summ % 89 != 0:
    summ = summ - ostatki[summ % 89]
    lensumm = lensumm - ostatkilen[summ % 89]

file = open('272_A.txt')
m = 0
l = 0
for n in file:
    n = int(n)
    m += n
    l += 1
    if m % 89 == 0:
        summ = m
        lensumm = l
    else:
        ms = m - ostatki[m % 89]
        l = lensumm - ostatkilen[m % 89]
        if ms == summ and l < lensumm:
            lensumm = l
print(l)


