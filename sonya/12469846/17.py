#Определите количество пар последовательности, в которых хотя бы одно число делится на минимальный элемент
# последовательности, кратный 21.
# Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.

file = open('107_17.txt')

min21 = 10000000

for n in file:
    n = int(n)
    if n % 21 == 0:
        min21 = min(min21, n)

file = open('107_17.txt')
count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if last % min21 == 0 or n % min21 == 0:
        count += 1
        maxsumm = max(maxsumm, n + last)
    last = n
print(count, maxsumm)
