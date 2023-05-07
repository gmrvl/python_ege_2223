file = open('р27.2_B.txt')
n = int(file.readline())
count = 0
ost0 = 0
ost26 = 0
ost13 = 0
ost2 = 0
for n in file:
    n = int(n)
    if n % 26 == 0:
        ost26 += 1
    elif n % 2 == 0:
        ost2 += 1
    elif n % 13 == 0:
        ost13 += 1
    else:
        ost0 += 1

count = ost2 * ost13 + ost26 * ost0 + ost26 * ost2 + ost26*ost13 + (ost26*(ost26 - 1))// 2

print(count)
