for x in range(0,10):
    s = int('8' + str(x) + '834',16)
    y = int('44' + str(x) + '27', 16)
    if (s+y) % 23 == 0:
        print((s+y)//23)

