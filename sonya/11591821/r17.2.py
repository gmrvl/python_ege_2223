#Определите количество троек чисел таких, которые могут являться сторонами остроугольного треугольника.
# В ответе запишите два числа: сначала количество найденных троек,
# а затем  — максимальную сумму элементов таких троек.

file =open('r17.2.txt')
count = 0
maxsumm = 0
plast = int(file.readline())
last = int(file.readline())
for n in file:
    n = int(n)
    if max(plast, last, n)**2 < min(plast, last, n)**2 + ((plast + last +  n) - min(plast, last, n) - max(plast, last, n))**2:
        count += 1
        maxsumm = max(maxsumm, last + plast + n)
    plast = last
    last = n
print(count, maxsumm)