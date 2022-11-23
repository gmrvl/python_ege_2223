file = open('17.1.txt')

last = -1
plast = -1
counts = 0
maxsumm = 0

for n in file:
    n = int(n)
    if last > -1 and plast > -1:
        if n**2 == last**2 + plast**2 or last**2 == n**2 + plast**2 or plast**2 == last**2 + n**2:
            counts += 1
            summ = n + last + plast
            if summ > maxsumm:
                maxsumm = summ
    last = n
    plast = last
if summ > maxsumm:
    maxsumm = summ
print(counts, maxsumm)