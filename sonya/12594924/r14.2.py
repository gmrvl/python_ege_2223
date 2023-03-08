for x in '0123456':
    for y in '0123456':
        s = int(y + x + '320', 7) + int('1' + x + '3' + y  + '3', 9)
        if s % 181 == 0:
            print(s // 181)

