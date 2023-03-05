#Определите количество троек чисел таких, которые могут являться сторонами остроугольного треугольника.
# В ответе запишите два числа: сначала количество найденных троек,
# а затем  — максимальную сумму элементов таких троек.

file = open('17.1.txt')
count = 0
maxcount = 0
maxsumm = 0
plast = int(file.readline())
last = int(file.readline())
for n in file:
    n = int(n)
    if max(n,plast,last)**2 < (min(n,plast,last)**2 + (n+plast+last - min(n,plast,last) - max(n,plast,last))**2):
        count += 1
        maxsumm = max(maxsumm, n + last + plast)
    plast = last
    last = n
print(count, maxsumm)