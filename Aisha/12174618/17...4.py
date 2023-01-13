file = open('17...4txt')

a = [int(i) for i in file]
count = 0
maxPair = 0
for i in range (len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] - a[j]) % 36 == 0 and (a[i] % 13 == 0 or a[j] % 13 == 0):
            count += 1
            m = max(maxPair, (a[i] - a[j]))

print(count, m)