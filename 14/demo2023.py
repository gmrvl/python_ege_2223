for i in range(0, 10):
    a = int('123' + str(i) + '5', 15)
    b = int('1' + str(i) + '233', 15)
    if (a + b) % 14 == 0:
        print((a + b) // 14)
        break
    # if 1**.... % 14 == 0:
    #     print(1**.... // 14)
    #     break

