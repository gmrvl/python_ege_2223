file= open('inf_22_10_20_27b.txt')
N = int(file.readline())
summ = 0
minraz = 10000000000
for i in file:
    x, y = map(int, i.split())
    summ += max(x,y)
    if abs(x - y) % 3 == 1:
        minraz = min(minraz, abs(x - y))
if summ % 3 == 1:
     print(summ - minraz)
