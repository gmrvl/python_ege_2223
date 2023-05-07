file = open('28131_B.txt')
n = int(file.readline())
ns = []
for i in file:
    i = int(i)
    ns.append(i)
maxsumm = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if (ns[i] + ns[j]) % 120 == 0 and (ns[i] > ns[j]) and (ns.index(ns[i]) < ns.index(ns[j])):
            maxsumm = max(maxsumm, ns[i] + ns[j])


for i in range(0, n):
    for j in range(i + 1, n):
        if (ns[i] + ns[j]) % 120 == 0 and (ns[i] > ns[j]) and (ns.index(ns[i]) < ns.index(ns[j])):
            if (ns[i] + ns[j]) == maxsumm:
                print(ns[i], ns[j])

