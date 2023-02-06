# Определите количество пар последовательности, в которых сумма элементов меньше минимального положительного элемента последовательности,
# кратного 19. Гарантируется. что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем абсолютное значение максимальной из сумм элементов таких пар.
file = open('17-339.txt')

min19 = 100000

for n in file:
    n = int(n)
    if n > 0:
        if n % 19 == 0:
            min19 = min(n, min19)

print(min19)

file = open('17-339.txt')
count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if n + last < min19:
        count += 1
        maxsumm = max(maxsumm, n + last)
    last = n
print(count,maxsumm)