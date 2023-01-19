#Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 60,
# затем максимальную из разностей элементов таких пар.


file = open('17 (1).txt')

maxraz = 0
count = 0
n = [int(i) for i in file]

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] - n[y]) % 60 == 0:
            count += 1
            maxraz = max(maxraz, n[x] - n[y])
print(count, maxraz)