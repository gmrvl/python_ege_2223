file = open('17.txt')

strings = [int(i) for i in file]
count = 0
maxsumm = 0

for x in range(0,len(strings) - 1):
    for y in range(x + 1, len(strings)):
        if (strings[x] - strings[y]) % 2 == 0 and (strings[x] % 19 == 0 or strings[y] % 19 == 0):
            count += 1
            maxsumm = max(maxsumm, strings[x] + strings[y])
print(count,maxsumm)