#Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 80,
# затем максимальную из разностей элементов таких пар.
file = open('r17.2.txt')

count = 0
maxraz = 0
n = [int(i) for i in file]

for x in range(0, len(n) - 1):
    for y in range(x + 1, len(n)):
        if abs(n[x] - n[y]) % 80 == 0:
            count += 1
            maxraz = max(maxraz, abs(n[x] - n[y]))
print(count, maxraz)