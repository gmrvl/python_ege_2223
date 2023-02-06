file = open('47231B.txt')

n = int(file.readline())
# считываем данные чтобы быстро иметь к ним доступ
data = []
for i in file:
    point, prob = map(int, i.split())
    if prob % 36 == 0:
        k = prob // 36
    else:
        k = prob // 36 + 1
    data.append([point, k])

min_sum = 10 ** 100000
# собираем массив с количеством ВСЕХ  контейнеров которые были слева (до этого пункта включительно)
total_prob = [data[0][1]]

for i in range(1, n):
    total_prob.append(total_prob[i-1] + data[i][1])

s = 0
# считаем стоимость перевозки в случае если лаборатория в 1 пункте

for i in range(1, n):
    s += abs(data[0][0] - data[i][0]) * data[i][1]

# для каждого пункта прибавляем к s стоимоть перевозок слева и вычитаем стоимость перевозок справа
for i in range(1, n):
    s = s + total_prob[i-1] * (data[i][0] - data[i-1][0]) - (data[i][0] - data[i-1][0]) * (total_prob[-1] - total_prob[i-1])
    min_sum = min(s, min_sum)

print(min_sum)
