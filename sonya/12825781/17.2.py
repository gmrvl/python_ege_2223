file =open('17.2.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 2 != 0:
        s += n
        i += 1
srarf = s // i

file = open('17.2.txt')
count = 0
maxsumm = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if (last % 5 == 0 and n < srarf) or (n % 5 == 0 and last < srarf):
        count += 1
        maxsumm = max(maxsumm, last + n)
    last = n
print(count, maxsumm)