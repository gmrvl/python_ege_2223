for x in '0123456789A':
    for y in '0123456789A':
        s = int('7' + y + '23' + x + '5', 25) + int('67' + x + '9' + y, 11)
        if s % 131 == 0:
            print(s // 131)