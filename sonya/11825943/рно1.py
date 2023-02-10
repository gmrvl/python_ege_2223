#Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 60 и хотя бы один из элементов кратен 15,
# затем максимальную из разностей элементов таких пар.

file = open('17.txt')

maxraz = 0
count = 0

n = [int(i) for i in file]

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if (n[x] - n[y]) % 60 == 0 and (n[x] % 15 == 0 or n[y] % 15 == 0):
            count += 1
            maxraz = max(maxraz, n[x] - n[y])
print(count, maxraz)




