file = open('17.txt')
min5 = 100000
for n in file:
    n = int(n)
    if 100 <= n < 1000:
        if n % 10 == 5:
            min5 = min(min5, n)
print(min5)
file = open('17.txt')
count = 0
maxsumm = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if (100 <= n < 1000 and last > 999) or ((n >= 1000) and 100 <= last < 1000):
        if (n + last) % min5 == 0:
            count += 1
            maxsumm = max(maxsumm, n + last)
            print(n**2, n, last ** 2, last, n + last)
    last = n
print(count, maxsumm, min5)