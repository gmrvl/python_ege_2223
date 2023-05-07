file = open('17.1.txt')
n = [int(i) for i in file]
count = 0
maxsumm = 0
for x in range(0,len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] * n[y]) % 26 == 0:
            summ = n[x] + n[y]
            count += 1
            maxsumm = max(maxsumm, summ)
print(count, maxsumm)

