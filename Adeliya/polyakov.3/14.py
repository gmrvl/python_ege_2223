for x in '0123456789ABCDE':
    s = int('131' + x + '1', 15) + int('13' + x + '3', 17)
    if s % 11 == 0:
        print(s // 11)
