file = open('26.txt')
K = int(file.readline())
N = file.readline()
ns = []
for n in file:
    s, v = map(int, n.split())
    ns.append([s, v])
ns = sorted(ns)
count = 0
maxtime = 0
nomer = 0
for i in range(K):
    time = 0
    for n in ns:
        if n[0] - time >= 1 and n[0] != 10**8 and n[1] != 10**8:
            count += 1
            time = n[1]
            if n[0] >= maxtime:
                maxtime = n[0]
                nomer = i + 1
            n[0] = 10**8
            n[1] = 10**8
print(count, nomer)
