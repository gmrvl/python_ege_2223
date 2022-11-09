for x in range(1, 7):
    for y in range(0, 7):
        first = int(str(x) + '01' + str(y) + '4', 9)
        second = int(str(x) + str(y) + '544', 8)
        summ = first + second
        if summ % 89 == 0:
            print(summ // 89)
