for x in range(1,10):
    for y in range(0,10):
        s = int(str(x) + '231' + str(y), 12) + int('78' + str(x) + '98' + str(y), 14)
        if s % 99 == 0:
            print(s//99)
            break