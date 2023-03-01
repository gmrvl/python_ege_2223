for x in '0123456789AB':
    for y in '0123456789AB':
        s = int(x + '231' + y, 12) + int('78' + x + '98' + y, 14)
        if s % 99 == 0:
            print(s // 99)
            break
