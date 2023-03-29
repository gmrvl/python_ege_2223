file = open('26.1.txt')
n = [int(i) for i in file]
count = 0
maxsumm = 0
ns = set(n)
for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] % 2 == 0 and n[y] % 2 != 0) or (n[y] % 2 == 0 and n[x] % 2 != 0):
            summ = n[x] + n[y]
            if summ in ns:
                count += 1
                maxsumm = max(maxsumm, summ)
print(count, maxsumm)