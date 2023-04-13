file = open('17.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 2 != 0:
        s += n
        i += 1
srarifm = s // i

count = 0
maxsumm = 0
file = open('17.txt')
last = int(file.readline())
for n in file:
    n = int(n)
    if (n % 5 == 0 and last < srarifm) or (last % 5 == 0 and n < srarifm):
        count += 1
        maxsumm = max(maxsumm, last + n)
    last = n
print(count, maxsumm)