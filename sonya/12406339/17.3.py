file = open('17 (2).txt')

count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if abs(n) % 3 == 0 or abs(last) % 3 == 0:
        count += 1
        maxsumm = max(maxsumm, n + last)
    last = n
print(count, maxsumm)