file = open('26.12.txt')
K = int(file.readline())
N = int(file.readline())
n = []
for i in file:
    x,y = map(int, i.split())
    n.append([x,y])
n = sorted(n)
count = 0
maxtime = 0
k = 0
for i in range(1, K + 1):
    time = 0
    for a in n:
        if a[0] - time >= 1 and a[1] != 0 and a[0] != 0:
            count += 1
            time = a[1]
            if maxtime < a[0]:
                maxtime = a[0]
                k = i
            a[1] = 0
            a[0] = 0
print(count, k)