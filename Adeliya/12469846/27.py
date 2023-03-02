file = open('27-B_2.txt')
n = file.readline()
maxx = 0

maxn = 0
max2 = 0
max7 = 0
max14=0
for n in file:
    n = int(n)
    maxn = max(maxn, n)
    if n % 14 == 0:
        max14 = max(max14, n)
    elif n % 7 == 0:
        max7 = max(max7, n)
    elif n % 2 == 0:
        max2 = max(max2, n)
    maxx=max(max14*maxn, max2 * max7)
print(maxx)
