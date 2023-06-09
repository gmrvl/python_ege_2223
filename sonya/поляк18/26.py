file = open('26-82.txt')
n = int(file.readline())
ns = []
for i in file:
    x,y = map(int, i.split())
    ns.append([x,y])
ns = sorted(ns)
count = 0
maxcount = 0
for i in range(1,n):
    if ns[i][0] == ns[i-1][0]:
        if ns[i][1] % 2 == 0:
            count += 1
        if ns[i-1][1] % 2 == 0:
            count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)
c = 0
for i in range(1,n):
    if ns[i][0] == ns[i-1][0]:
        if ns[i][1] % 2 == 0:
            c += 1
        if ns[i-1][1] % 2 == 0:
            c += 1
    else:
        if c == maxcount:
            print(ns[i][0])
            break
        c = 0
