file = open('172.txt')
plast = int(file.readline())
last = int(file.readline())
count = 0
maxsumm = 0
for n in file:
    n = int(n)
    if (max(plast, last, n))**2 < ((n + last + plast - max(plast, last, n) - min(plast, last, n))**2 + (min(plast, last, n))**2):
        count += 1
        maxsumm = max(maxsumm, n + plast + last)
    plast = last
    last = n
print(count, maxsumm)

