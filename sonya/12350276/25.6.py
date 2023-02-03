for v in range(0,10):
    for z in range(0, 1000):
        s = int('1' + str(v) +'2139' + str(z) + '4')
        if s % 2023 == 0:
            print(s, s // 2023)


