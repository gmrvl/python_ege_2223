file = open()

total_sum = 0
max_sum = 0
min_sum = 0

min1 = 10 ** 10 # на случай ЧЧ
min2 = 10 ** 10 # на случай НН
min3 = 10 ** 10 # на случай НЧ

for i in file:
    x, y = map(int, i.split(' '))
    total_sum += x, y
    if x > y:
        max_sum += x
        min_sum += y
        if x % 2 == 0 and y % 2 == 1:
            min1 = min(min1, x + y)

