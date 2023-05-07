file=open('26.2.txt')
n, m = map(int, file.readline().split(' '))
ns = []
count = 0
a = 0
for i in file:
    i = int(i)
    if 200 <= i <= 210:
        a += i
        count += 1
    else:
        ns.append(i)

ns = sorted(ns)
for i in ns:
    if a + i <= m:
        count += 1
        a += i
    else:
        break
maxx = 0
for i in range(count, len(ns)):
    if (a - ns[count - 1]) + ns[i] <= m:
        maxx = ns[i]
    else:
        break
a = a - ns[count - 1] + maxx
print(count, a)




