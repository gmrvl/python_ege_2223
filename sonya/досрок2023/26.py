file = open('26.txt')
K = int(file.readline())
N = int(file.readline())
a = []
for i in file:
    sdacha, vidacha = map(int, i.split())
    a.append([sdacha, vidacha])
a.sort()
count = 0
maxtime = 0
maxk = 0
for i in range(1, K + 1):
    time = 0
    for n in a:
        if n[0] - time >= 1 and n[1] != 10**8 and n[0] != 10**8:
            count += 1
            time = n[1]
            if n[0] >= maxtime:
                maxtime = n[0]
                maxk = i
            n[0] = 10**8
            n[1] = 10**8
print(count, maxk)


