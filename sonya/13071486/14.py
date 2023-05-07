for x in '0123456789AB':
    for y in '0123456789AB':
        s = int(y + 'AA' + x, 12) + int(x + '02' + y, 14)
        if s % 80 == 0:
            print(s // 80)