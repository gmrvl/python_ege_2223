for x in '0123456789':
    s = int('55' + x + '36', 19) + int(x + '2724', 19)
    if s % 11 == 0:
        print(s // 11)
        break