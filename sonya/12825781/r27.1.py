file = open('271-B.txt')
N = int(file.readline())
ns =[]

for i in file:
    mi, ma = map(int, i.split())
    ns.append([mi, ma])

summ = 0
ch = 0
nch = 0
for i in range(N):
    summ += min(ns[i][0], ns[i][1])
    if min(ns[i][0], ns[i][1]) % 2 == 0:
        ch += 1
    else:
        nch += 1
print(ch, nch, summ)
ch1 = ch
nch1 = nch
minsumm = 1000**100
if ch > nch:
    if (summ % 2) == 0:
        print(summ)
else:
    if (summ % 2) == 1:
        print(summ)
for i in range(N):
    summ1 = summ - min(ns[i][0], ns[i][1])
    if min(ns[i][0], ns[i][1]) % 2 == 0:
        ch1 = ch - 1
    else:
        nch1 = nch - 1
    summ1 = summ1 + max(ns[i][0], ns[i][1])
    if max(ns[i][0], ns[i][1]) % 2 == 0:
        ch1 = ch + 1
    else:
        nch1 = nch + 1
    if ch1 > nch1:
        if (summ1 % 2) == 0:
            minsumm = min(minsumm, summ1)
    else:
        if (summ % 2) == 0:
            minsumm = min(minsumm, summ1)
print(minsumm)
