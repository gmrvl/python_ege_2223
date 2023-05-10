file = open('33528.txt')

n, money = map(int, file.readline().split())

b = []
for i in file:
    price, count, type = i.split()
    if type == 'A':
        money -= int(price) * int(count)
    else:
        b.append([int(price), int(count)])
b = sorted(b)
index = ''
c = 0
total_count_b = 0

for i in range(len(b)):
    if money - b[i][0] * b[i][1] >= 0:
        money -= b[i][0] * b[i][1]
        total_count_b += b[i][1]
        print(money)
    else:
        index = i
        c = b[i][1]
        break # тут была ошибка

for i in range(c - 1, 0, -1):
    if money - b[index][0] * i >= 0:
        money -= b[index][0] * i
        total_count_b += i
# красиво посчитать без цикла можно так:
# if c != 0:
#     total_count_b += money // b[index][0]
#     money = money - (money // b[index][0] * b[index][0])
print(total_count_b, money)
