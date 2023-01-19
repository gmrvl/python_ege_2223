#Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 45 и хотя бы один из элементов кратен 18,
# затем максимальную из разностей элементов таких пар.

file = open('17 (3).txt')

n = [int(i) for i in file]

count = 0
maxraz = 0

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if abs(n[x] - n[y]) % 45 == 0 and (n[x] % 18 == 0 or n[y] % 18 == 0):
            count += 1
            maxraz = max(maxraz, abs(n[x] - n[y]))
print(count,maxraz)
