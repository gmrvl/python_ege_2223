#Определите количество пар, в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
# В ответе запишите два числа: сначала количество найденных пар, а затем  — максимальную сумму элементов таких пар.

file = open('r17.txt')

count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if n % 5 == 0 or last % 5 == 0:
        if (n + last) % 7 == 0:
            count += 1
            maxsumm = max(maxsumm, n + last)
    last = n
maxsumm = max(maxsumm, n + last)
print(count,maxsumm)