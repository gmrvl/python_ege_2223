file = open('26.6.txt')
s, n = map(int, file.readline().split(' '))
a = []
for i in file:
    a.append(int(i))
a = sorted(a)
c = 0
summ = 0

for i in range(len(a)):
    if a[i] + summ <= s:
        summ += a[i]
    else:
        c = i
        break
maxx = 0
for i in range(c, n):
    if (summ - a[c - 1]) + a[i] <= s:
        maxx = a[i]
    else:
        break
print(c, maxx)
