# Определите количество пар,
# в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
file = open('17 (4).txt')
count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if (n % 5 == 0 or last % 5 == 0) and (n + last) % 7 == 0:
        count += 1
        maxsumm = max(maxsumm, n + last)
    last = n
print(count, maxsumm)
