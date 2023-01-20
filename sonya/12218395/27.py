file = open('27-B_2.txt')
n = file.readline()


maxX = 0
max0 = 0
max2 = 0
max7 = 0

for x in file:
    x = int(x)
    if x % 14 == 0:
        max0 = max(max0, x)

file = open('27-B_2.txt')
n = file.readline()

for xx in file:
    xx = int(xx)
    if xx != max0:
        maxX = max(xx, maxX)

file = open('27-B_2.txt')
n = file.readline()

for i in file:
    i = int(i)
    if i % 2 == 0 and i % 14 != 0:
        max2 = max(max2, i)
    if i % 7 == 0 and i % 14 != 0:
        max7 = max(max7, i)


print(max(max0*maxX, max7 * max2))


