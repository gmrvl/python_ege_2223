for x in '012345678':
    for y in '012345678':
        s = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if s % 61 == 0:
            print(s // 61)