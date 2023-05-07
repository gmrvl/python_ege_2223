for x in '0134567':
    for y in '1234567':
        s = int(str(y) + '04' + str(x) + '5', 11) + int('253' + str(x) + str(y), 8)
        if s % 117 == 0:
            print(s // 117)