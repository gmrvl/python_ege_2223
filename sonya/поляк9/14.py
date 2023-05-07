for x in '0123456789ABCDEFG':
    s = int('9759' + x, 17) + int('3' + x + '108', 17)
    if s % 11 == 0:
        print(s//11)