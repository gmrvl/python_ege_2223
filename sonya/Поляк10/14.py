for x in '0123456789AB':
    s = int('19' + x + '61', 12) + int('3393' + x, 17)
    a = int('60' + x + '05', 15)
    if s == a:
        print(a)