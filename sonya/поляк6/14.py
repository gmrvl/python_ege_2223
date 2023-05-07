for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        s = int('123' + x + '5', 15) + int('67' + y + '9', 17)
        if s % 131 == 0:
            print(s // 131, x ,y)
