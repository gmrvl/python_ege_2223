file = open('26.8.txt')
N = int(file.readline())
n = []
for i in file:
    r, m = map(int, i.split())
    n.append([r,m])
n = sorted(n)
ryad = 0
minmesto = 0
for i in range(1, N):
    if n[i][0] == n[i-1][0]:
        if n[i][1] - n[i-1][1] == 14:
            ryad = n[i][0]
            minmesto = n[i-1][1] + 1
print(ryad, minmesto)