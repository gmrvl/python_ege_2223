#пределите и запишите в ответе сначала количество пар элементов последовательности,
# для которых произведение элементов кратно 26,
# затем максимальную из сумм элементов таких пар.

file = open('17 (1).txt')

count = 0
maxsumm = 0

n = [int(i) for i in file]

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] * n[y]) % 26 == 0:
            maxsumm = max(maxsumm, n[x] + n[y])
            count += 1
print(count,maxsumm)