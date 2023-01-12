for x in '0123456789':
    s = int('4C' + x + '4', 15) + int(x + '62A', 13)
    if s % 121 == 0:
        print(s // 121)
        break