file = open('inf_26_04_21_27b.txt')
n = int(file.readline())

maxn = []
minn = []
for i in file:
    x, y = map(int, i.split())
    if y % 2 == 1:
        minn.append(min(x,y))
        maxn.append(max(x,y))

#A
# minn[2] = 0
# maxn[2] = 0

print(sum(maxn), sum(minn))
# из больших надо вычесть нечетное, из меньших четное

a = [] #наим из болших нечетное и его нечетная пара из меньших
b = [] #наим нечетное из наименьших и его нечетная пара из наибольших

maxnsorted = sorted(maxn)
for i in maxnsorted:
    if maxn[maxn.index(i)] % 2 == 1:
        if minn[maxn.index(i)] % 2 == 1:
            a.append([maxn[maxn.index(i)], minn[maxn.index(i)]])
            break

minnsorted = sorted(minn)
for i in minnsorted:
    if minn[minn.index(i)] % 2 == 1:
        if maxn[minn.index(i)] % 2 == 1:
            b.append([minn[minn.index(i)], maxn[minn.index(i)]])
            break

print(a,b)
maxsumm = sum(maxn) + sum(minn) - min(a[0][0] + a[0][1], b[0][1] + b[0][1])
print(maxsumm)



