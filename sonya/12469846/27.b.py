file = open('27-B_2.txt')

n = file.readline()
maxX = 0

maxn = 0
max0 = 0
max2 = 0
max7 = 0
for n in file:
    n = int(n)
    maxn = max(maxn, n)
    if n % 14 == 0:
        max0 = max(max0, n)
    elif n % 7 == 0:
        max7 = max(max7, n)
    elif n % 2 == 0:
        max2 = max(max2, n)
print(max(max0*maxn, max2 * max7))
