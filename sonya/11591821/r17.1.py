#Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых разность элементов кратна 45 и хотя бы один из элементов кратен 18,
# затем максимальную из разностей элементов таких пар.

file = open('r17.1.txt')
count = 0
maxraz = 0
a = [int(i) for i in file]
for x in range(0,len(a)-1):
    for y in range(x+1,len(a)):
        if a[x] % 18 == 0 or a[y] % 18 == 0:
            if abs(a[x] - a[y]) % 45 == 0:
                count += 1
                maxraz = max(maxraz, abs(a[x] - a[y]))
print(count, maxraz)