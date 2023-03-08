for x in '0123456789AB':
    for y in '0123456789AB':
        s = int(str(x) + '231' + str(y), 12) + int('78' + str(x) + '98' + str(y), 14)
        if s % 99 == 0:
            print(s//99)
