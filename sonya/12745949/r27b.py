file = open('р27-B.txt')
n = int(file.readline())
summ3 = []
k = 0
raz = 10*10
for i in file:
    x, y, z = map(int, i.split())
    a = max(x,y,z)
    c = min(x,y,z)
    b = x + y + z - a - c
    summ3.append(c)
    if (a+b) % 2 != 0:
        k += 1
        if (a+c) % 2 != 0:
            raz = min(raz, abs(a-c))
        else:
            raz = min(raz, abs(a - b))
if k % 2 != 0:
    print(sum(summ3))
else:
    print(sum(summ3) + raz)
