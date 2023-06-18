file = open('2-27-B_demo.txt')
N = int(file.readline())
summ = 0
minraz = 100000000
for i in file:
    x, y = map(int, i.split())
    summ += max(x,y)
    if abs(x - y) % 3 != 0:
        minraz = min(minraz, abs(x - y))
if summ % 3 == 0:
    print(summ - minraz)



