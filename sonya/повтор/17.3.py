file = open('173.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 2 == 0:
        s += n
        i += 1
srarfm = s // i
file = open('173.txt')
last = int(file.readline())
count = 0
maxsumm = 0
for n in file:
    n = int(n)
    if (n % 3 == 0 and last < srarfm) or (last % 3 == 0 and n < srarfm):
        count += 1
        maxsumm = max(maxsumm, last + n)
    last = n
print(count, maxsumm)
