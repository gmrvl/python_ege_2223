file = open('17.txt')
a = [int(i) for i in file]
count = 0
maxx = 0
s = 0
n = 0
for i in range(len(a)):
    if (a[i] % 2 == 1):
        s += a[i]
        n += 1
x = s / n
for i in range(len(a) - 1):
    if ((a[i] % 5 == 0) or (a[i + 1] % 5 == 0)) and ((a[i] < x) or (a[i + 1] < x)):
        count += 1
        maxx = max(maxx, a[i] + a[i + 1])
print(count, maxx)