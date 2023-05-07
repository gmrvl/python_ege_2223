file = open('27-B.txt')
N = int(file.readline())
ostatki = [0 for i in range(10)]

maxsumm = 0
summ = 0
chet = 0
for n in file:
    n = int(n)
    summ += n
    if n % 2 == 0:
        chet += 1
    if chet % 10 == 0:
        maxsumm = max(maxsumm, summ)
    else:
        if ostatki[chet % 10] == 0:
            ostatki[chet % 10] = summ
        maxsumm = max(maxsumm, summ - ostatki[chet % 10])
print(maxsumm)
