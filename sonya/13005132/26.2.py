file = open ('26.2.txt')
N = int(file.readline())
a = []
for i in file:
    ryad, nomer = map(int, i.split())
    a.append([ryad, nomer])
a = sorted(a)
maxryad = 0
minnomer = 0
for i in range(1, N):
    if a[i][0] == a[i-1][0]:
        if a[i][1] - a[i-1][1] == 3:
            maxryad = a[i][0]
            minnomer = a[i-1][1] + 1
print(maxryad, minnomer)
