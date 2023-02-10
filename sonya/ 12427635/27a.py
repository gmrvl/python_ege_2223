file = open('107_27_A.txt')

n = int(file.readline())

a = []
for i in file:
    a.append(int(i)*3)

minn = 10 ** 10000000
for i in range(0, n - 1):
    zatrat = 0
    for j in range(0, n - 1):
        zatrat += a[j]
    zatrat = zatrat - a[i]
    minn = min(minn, zatrat)
print(minn)