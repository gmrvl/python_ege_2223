#Определите количество пар, в которых хотя бы один из двух элементов делится на 3 и
# хотя бы один из двух элементов меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар,
# а затем  — максимальную сумму элементов таких пар.
file = open('17.2.txt')
s = 0
i = 0
for n in file:
    n = int(n)
    if n % 2 == 0:
        s += n
        i += 1
srarifm = s // i
file = open('17.2.txt')
count = 0
maxsumm = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if n % 3 == 0 or last % 3 == 0:
        if n < srarifm or last < srarifm:
            count += 1
            maxsumm = max(maxsumm, last + n)
    last = n
print(count, maxsumm)