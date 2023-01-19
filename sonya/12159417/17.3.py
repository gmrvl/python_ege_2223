#Определите количество пар последовательности, в которых только одно число оканчивается на 3,
# а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на 3.
# В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную из сумм квадратов элементов таких пар.

file = open('17 (2).txt')

maxtri = 0

for i in file:
    i = int(i)
    if i % 10 == 3:
        maxtri = max(maxtri, i)

print(maxtri)

file = open('17 (2).txt')

last = 0
count = 0
maxsumm = 0

for n in file:
    n = int(n)
    if ((n % 10 == 3 or n % 10 == -3) and (last % 10 != 3 and last % 10 != -3)) or ((last % 10 == 3 or last % 10 == -3) and (n % 10 != 3 and n % 10 != -3)):
        if (n ** 2 + last ** 2) >= maxtri ** 2:
            count += 1
            maxsumm = max(maxsumm, n ** 2 + last ** 2)
    last = n
print(count, maxsumm)
