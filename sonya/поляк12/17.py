file = open('17-328 (1).txt')
max50 = 0
for n in file:
    n = int(n)
    if n % 50 == 0:
        max50 = max(max50, n)

file = open('17-328 (1).txt')
count = 0
maxsumm = 0
plast = int(file.readline())
last = int(file.readline())
for n in file:
    n = int(n)
    summ1 = plast + last
    summ2 = plast + n
    summ3 = n + last
    if str(summ1) == ''.join(reversed(str(summ1))) and str(summ2) == ''.join(reversed(str(summ2))) and str(summ3) == ''.join(reversed(str(summ3))):
        if max(summ1,summ2,summ3) < max50:
            count += 1
            maxsumm = max(maxsumm, plast + last + n)
    plast = last
    last = n
print(count, maxsumm)