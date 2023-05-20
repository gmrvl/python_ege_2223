file = open('17.txt')
count = 0
maxx = 0
a = [int(i) for i in file]
minA = 100000
for i in a:
    if i % 10 == 5 and 99 < i < 1000:
        minA = min(minA, i)
for i in range(len(a) - 1):
    if 100 <= a[i] <= 999 or 100 <= a[i + 1] <= 999:
        if (a[i] + a[i + 1]) % minA == 0:
            print(a[i] + a[i + 1])
            count += 1
            maxx = max(maxx, a[i] + a[i + 1])
print(maxx, count)
