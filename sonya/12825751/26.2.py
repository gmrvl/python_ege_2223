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
ns2 = []
for i in ns:
    if m + i <= M:
        count2 += 1
        m += i
        ns2.append(i)
    else:
        break
count22 = count2
k = len(ns) - 1
while count2 > 0:
    while k >= 0:
        if sum(ns2) - ns2[count2-1] + ns[k] <= M and ns[k] != 0:
            ns2[count2-1] = ns[k]
            ns[k] = 0
            count2 -= 1
            break
        else:
            k -= 1
print(count1 + count22, sum(ns2))





