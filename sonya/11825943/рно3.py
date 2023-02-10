# Определите количество пар последовательности, в которых только одно число оканчивается на 3,
# а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на 3.
# В ответе запишите два числа:
# сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар.

file = open('17 (2).txt')
max3 = 0

for n in file:
    n = int(n)
    if abs(n) % 10 == 3:
        max3 = max(max3, n)
print(max3)

file = open('17 (2).txt')
count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if (abs(n % 10) == 3 and abs(last % 10) != 3) or (abs(last % 10) == 3 and abs(n % 10) != 3):
        if (n**2 + last**2) >= max3*max3:
            count += 1
            maxsumm = max(maxsumm, n**2 + last**2)
    last = n
print(count,maxsumm)

