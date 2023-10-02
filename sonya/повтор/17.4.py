file = open('174.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 2 == 1:
        s += n
        i += 1
srarfm = s // i
file = open('173.txt')
last = int(file.readline())
count = 0
maxsumm = 0
for n in file:
    n = int(n)
    if (n % 5 == 0 and last < srarfm) or (last % 5 == 0 and n < srarfm):
        count += 1
        maxsumm = max(maxsumm, last + n)
    last = n
print(count, maxsumm)