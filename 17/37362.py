file = open('37362.txt')

count = 0
maxCount = 0

a = []
for i in file:
    a.append(int(i))

for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] + a[j]) % 80 == 0) and (a[i] % 50 == 0 or a[j] % 50 == 0):
            count += 1
            maxCount = max(maxCount, a[i] + a[j])
print(count, maxCount)