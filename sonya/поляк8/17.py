# (№ 5248)
file = open('17-324.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 37 != 0:
        s += n
        i += 1
srarifm = s // i

file = open('17-324.txt')
plast = int(file.readline())
last = int(file.readline())
count = 0
maxsumm = 0
for n in file:
    n = int(n)
    summ = plast + last + n
    summ2 = bin(summ)[2:]
    # summ2 = list(summ2)
    res = ''.join(reversed(summ2))
    if summ2 == res:
        if min(plast, last, n) > srarifm:
            count += 1
            maxsumm = max(maxsumm, last + plast + n)
    plast = last
    last = n
print(count, maxsumm)
