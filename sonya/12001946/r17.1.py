#Определите и запишите в ответе сначала количество пар элементов последовательности,
# разность которых четна и хотя бы одно из чисел делится на 19,
# затем максимальную из сумм элементов таких пар.
file = open('r17.1.txt')

count = 0
maxsumm = 0
n = [int(i) for i in file]

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if abs(n[x] - n[y]) % 2 == 0 and (n[x] % 19 == 0 or n[y] % 19 == 0):
            count += 1
            maxsumm = max(maxsumm, n[x] + n[y])
print(count, maxsumm)