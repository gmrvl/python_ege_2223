file = open('27-A_2.txt')

n = file.readline()
a = [int(i) for i in file]
maxX = 0

for x in range(0, len(a) - 1):
    for y in range(x+1, len(a)):
        if a[x]*a[y] % 14 == 0:
            maxX = max(maxX, a[x] * a[y])
print(maxX)
