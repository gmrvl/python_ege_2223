file = open('17.txt')

count = 0
maxsumm = 0

n = [int(i) for i in file]

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] + n[y]) % 80 == 0:
            if n[x] % 50 == 0 or n[y] % 50 == 0:
                count += 1
                maxsumm = max(maxsumm, n[x] + n[y])
print(count,maxsumm)
