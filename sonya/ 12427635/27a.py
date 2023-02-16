file = open('107_27_A.txt')

n = int(file.readline())

a = []
for i in file:
    a.append(int(i))

minn = 10 ** 10000000
for i in range(0, n):
    zatrat = 0

    for j in range(0, n):
        if i > n // 2:
            if j <= abs(i - (n // 2)):
                zatrat += (n - (i - j)) * 3 * a[j]
            else:
                zatrat += a[j] * abs(i-j) * 3
        else:
            if j >= abs(i + (n // 2)):
                zatrat += (n - (i - j)) * 3 * a[j]
            else:
                zatrat += a[j] * abs(i-j) * 3

    # zatrat = zatrat - a[i]
    minn = min(minn, zatrat)
print(minn)
