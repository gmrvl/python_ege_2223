count = 0
for i in range(100, 1000):
    first = i // 100
    second = (i // 10) % 10
    third = i % 10
    sum_1_2 = first + second
    sum_2_3 = second + third
    if sum_1_2 > sum_2_3:
        res = str(sum_2_3) + str(sum_1_2)
    else:
        res = str(sum_1_2) + str(sum_2_3)
    if res == '1216':
        count += 1
print(count)