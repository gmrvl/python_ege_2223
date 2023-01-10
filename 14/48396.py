for x in '0123456789ABCDEF':
    s = int('2' + x + '84', 19) + int('2B3' + x, 16)
    if s % 88 == 0:
        print(s // 88)
        break