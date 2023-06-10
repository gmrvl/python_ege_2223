file = open('27881.txt')
s,n = map(int, file.readline().split())

a = []
for i in file:
    a.append(int(i))
a = sorted(a)
count = 0
for i in range(n):
    if s - a[i] >= 0:
        s -= a[i]
        count += 1
    else:
        break
maxx = 0
for i in range(count, n):
    if s + a[count - 1] - a[i] >= 0:
        maxx = a[i]
    else:
        break
print(count, maxx)