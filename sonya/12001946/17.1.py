# Определите и запишите в ответе сначала количество пар элементов последовательности,
#  у которых разность элементов кратна 60
# затем максимальную из разностей элементов таких пар
file = open('17.1.txt')

strings = [int(i) for i in file]
count = 0
maxraz = 0

for x in range(0, len(strings) - 1):
    for y in range(x + 1, len(strings)):
        if (strings[x] - strings[y]) % 60 == 0:
            count += 1
            maxraz = max(maxraz, strings[x] - strings[y])
print(count, maxraz)
