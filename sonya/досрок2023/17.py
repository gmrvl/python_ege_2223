file = open('17.txt')
min5 = 100000
for n in file:
    if len(n) == 3:
        if n[-1] == '5':
            min5 = min(min5, int(n))
file = open('17.txt')
count = 0
maxsumm = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if (len(str(n)) == 3 and len(str(last)) != 3) or (len(str(n)) != 3 and len(str(last)) == 3):
        if (n + last) % min5 == 0:
            count += 1
            maxsumm = max(maxsumm, n**2 + last ** 2)
    last = n
print(count, maxsumm, min5)