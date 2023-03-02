file=open('17.txt')
a = [int(i) for i in file]
count = 0
maxx = 0
s = 0
k = 0
for i in range(len(a)):
    if (a[i] % 2 == 0):
        s += a[i]
        k += 1
x = s / k
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) or (a[i + 1] % 3 == 0)) and ((a[i] < x) or (a[i + 1] < x)):
        count += 1
        maxx = max(maxx, a[i] + a[i + 1])
print(count, maxx)