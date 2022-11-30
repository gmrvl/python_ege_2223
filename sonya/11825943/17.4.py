file = open('17.1.txt')

plast = int(file.readline())
last = int(file.readline())
counts = 0
maxsumm = 0

for n in file:
    n = int(n)
    summ = 0
    if n**2 == last**2 + plast**2 or last**2 == n**2 + plast**2 or plast**2 == last**2 + n**2:
        counts += 1
        summ = n + last + plast
        if summ > maxsumm:
            maxsumm = summ
    plast = last
    last = n

if summ > maxsumm:
    maxsumm = summ
print(counts, maxsumm)