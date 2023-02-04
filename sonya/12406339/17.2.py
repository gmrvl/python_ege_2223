file = open('17 (1).txt')
count = 0
maxsumm = 0
n = [int(i) for i in file]
for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        summ = n[x] + n[y]
        if summ % 9 == 0:
            count += 1
            maxsumm = max(maxsumm,summ)
print(count, maxsumm)