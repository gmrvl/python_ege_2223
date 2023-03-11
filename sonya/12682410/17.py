# Назовём парой два идущих подряд элемента последовательности. Определите количество пар,
# в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
# В ответе запишите два числа: сначала количество найденных пар,
# а затем  — максимальную сумму элементов таких пар.

file = open('17.txt')
maxsumm = 0
count = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if n % 5 == 0 or last % 5 == 0:
        summ = n + last
        if summ % 7 == 0:
            count += 1
            maxsumm = max(maxsumm, summ)
    last = n
print(count, maxsumm)