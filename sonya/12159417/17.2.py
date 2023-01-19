#Определите и запишите в ответе сначала количество пар элементов последовательности,
# для которых произведение элементов делится без остатка на 10,
# затем максимальную из сумм элементов таких пар.
file = open('17 (1).txt')

n = [int(i) for i in file]

count = 0
maxsumm = 0

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] * n[y]) % 10 == 0:
            count += 1
            maxsumm = max(maxsumm, n[x] + n[y])
print(count, maxsumm)