for x in '0123456789A':
    s = int( '3' + x + 'D' + 'A', 14) + int('5' + x + 'A' + '6', 12)
    if s % 81 == 0:
        print ( s // 81)
        break