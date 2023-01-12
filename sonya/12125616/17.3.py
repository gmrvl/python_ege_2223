#Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 9,
# затем максимальную из сумм элементов таких пар.

file = open('17.3.txt')

strings = [int(i) for i in file]
count = 0
maxsumm = 0

for x in range(0, len(strings) - 1):
    for y in range(x + 1, len(strings)):
        if (strings[x] + strings[y]) % 9 == 0:
            count += 1
            maxsumm = max(maxsumm, strings[x] + strings[y])
print(count,maxsumm)