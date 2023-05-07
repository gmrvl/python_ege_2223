file = open('272_A.txt')
N = int(file.readline())
ostatki = [10000000 for i in range(89)]
ostatkilen = [0 for z in range(89)]
summ = 0
summl = 0
maxsumm =0
minlen = 0
ms = 0
l = 0
for n in file:
    n = int(n)
    summ += n
    summl += 1
    d = summ % 89
    if d == 0:
        maxsumm = summ
        minlen = summl
    else:
        ms = summ = ostatki[d]
        l = minlen - ostatkilen[d]
        if ms > maxsumm:
            maxsumm = ms
            minlen = l
        if ms == maxsumm and l < minlen:
            maxsumm = ms
            minlen = l
    if summ < ostatki[d]:
        ostatki[d] = summ
        ostatkilen[d] = summl
print(minlen)