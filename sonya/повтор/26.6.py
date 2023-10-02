file = open('26.6.txt')
N = int(file.readline())
n = []
for i in file:
    r, m = map(int, i.split())
    n.append([r,m])
n = sorted(n)
ryad = 0
mestomin = 0
for i in range(1, N):
    if n[i][0] == n[i - 1][0]:
        if n[i][1] - n[i - 1][1] == 3:
            ryad = n[i][0]
            mestomin = n[i-1][1] + 1
print(ryad, mestomin)

