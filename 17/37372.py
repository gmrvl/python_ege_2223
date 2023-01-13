file = open('37372.txt')
strings = [int(i) for i in file]

count = 0
maxPair = 0

for x in range(0, len(strings)-1):
    for y in range(x + 1, len(strings)):
        if (strings[x] - strings[y]) % 45 == 0 and (strings[x] % 18 == 0 or strings[y] % 18 == 0):
            count += 1
            maxPair = max(maxPair, strings[x] - strings[y])
print(count, maxPair)