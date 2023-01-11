file = open('37341.txt')

a = [int(i) for i in file]
count = 0
maxPair = 0
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] - a[j]) % 2 == 0 and (a[i] % 19 == 0 or a[j] % 19 == 0):
            count += 1
            maxPair = max(maxPair, a[i] + a[j])

print(count, maxPair)
