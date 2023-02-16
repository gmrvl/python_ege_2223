for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        s = int('90' + x + '4' + y, 15) + int('91' + x + y + '2', 16)
        if s % 56 == 0:
            print(s // 56)
            break