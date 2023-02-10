file = open('107_27_B.txt')

n = int(file.readline())

a = [] #цена от пункта до пункта

for i in file:
    a.append(int(i) * 3)

do = []
do.append(a[0])
for i in range(1, n - 1):
    do.append(do[i-1] + a[i])


zatrat = 0
for i in range(0, n - 1):
    zatrat += a[i]

minn = 10 * 10000000

for i in range(1, n - 1):
    zatrat = zatrat + do[i-1] - (do[-1] - do[i-1])
    minn = min(minn, zatrat)
print(minn)

