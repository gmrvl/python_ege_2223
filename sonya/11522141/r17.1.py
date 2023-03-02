#Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма нечётна,
# а произведение делится на 5,
# затем максимальную из сумм элементов таких пар.

file = open('17.txt')

count = 0
maxsumm = 0

n = [int(i) for i in file]
for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] + n[y]) % 2 == 1 and (n[x] *n[y]) % 5 == 0:
            count += 1
            maxsumm = max(maxsumm, n[x] + n[y])
print(count, maxsumm)

