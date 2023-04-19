file = open('26.2.txt')
N, M = map(int, file.readline().split())
ns = []
count1 = 0
m = 0
for i in file:
    i = int(i)
    if 200 <= i <= 210:
        m += i
        count1 += 1
    else:
        ns.append(i)

ns = sorted(ns)
count2 = 0
for i in ns:
    if m + i <= M:
        count2 += 1
        m += i
    else:
        break
maxx = 0
m = (m - ns[count2 - 1])
for i in range(count2 - 1, len(ns)):
    if m + ns[i] <= M:
        maxx = ns[i]
    else:
        break
maxx2 = 0
m = m - ns[count2 - 2] + maxx
for i in range(count2 - 1, len(ns)):
    if m + ns[i] <= M:
        maxx2 = ns[i]
    else:
        break

m = m + maxx2
print(count1 + count2, m)




