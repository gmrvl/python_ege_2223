file = open('38960.txt')  # считывание входных данных
n, maxsum = map(int, file.readline().split(' '))
data = []
for i in file:
    x, y = i.split()
    data.append([int(x), y])

# создаём отдельные массивы для изделий a и b, и сортируем все 3 массива
alist = [k[0] for k in data if k[1] == 'A']
blist = [k[0] for k in data if k[1] == 'B']

alist.sort()
blist.sort()
data.sort()
# data.sort(key=lambda k: k[0])

# считаем максимальное количество изделий
msum = 0
maxc = 0

for i in data:
    if msum + i[0] <= maxsum:
        msum += i[0]
        maxc += 1
    else:
        break

# "закупаем" максимальное количество изделий A
buied_a = []

for i in alist:
    if len(buied_a) >= maxc: break
    if sum(buied_a) + i <= maxsum:
        buied_a.append(i)
    else:
        break

# докупаем изделия B, при необходимости удаляя изделия A, пока не доберём до максимального значения
buied_b = []

for i in blist:
    if len(buied_a) + len(buied_b) >= maxc: break
    if sum(buied_a) + sum(buied_b) + i <= maxsum:
        buied_b.append(i)
    else:
        while sum(buied_a) + sum(buied_b) + i > maxsum:
            del buied_a[-1]
        buied_b.append(i)

# вывод ответа
print(len(buied_a))
print(maxsum - (sum(buied_a) + sum(buied_b)))
