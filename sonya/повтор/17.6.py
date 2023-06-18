file = open('1_17.txt')
max2 = 0
for n in file:
    n = int(n)
    if 9 < n < 100:
        max2 = max(max2, n)

file = open('1_17.txt')
last = int(file.readline())
count = 0
maxsumm = 0
for n in file:
    n = int(n)
    if (9 < n < 100) != (9 < last < 100):
        if (n + last) % max2 == 0:
            count += 1
            maxsumm = max(maxsumm, n + last)
    last = n
print(count, maxsumm)
